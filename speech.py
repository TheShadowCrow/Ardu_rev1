from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave
import audiotools 
import os
import urllib2
import urllib
import time
class Speech: 

	THRESHOLD = 500
	CHUNK_SIZE = 1024
	FORMAT = pyaudio.paInt16
	RATE = 44100

	def is_silent(snd_data):
		#"Returns 'True' if below the 'silent' threshold"
		return max(snd_data) < THRESHOLD

	def normalize(snd_data):
		#"Average the volume out"
		MAXIMUM = 16384
		times = float(MAXIMUM)/max(abs(i) for i in snd_data)

		r = array('h')
		for i in snd_data:
			r.append(int(i*times))
		return r

	def trim(snd_data):
		#"Trim the blank spots at the start and end"
		def _trim(snd_data):
			snd_started = False
			r = array('h')

			for i in snd_data:
				if not snd_started and abs(i)>THRESHOLD:
					snd_started = True
					r.append(i)

				elif snd_started:
					r.append(i)
			return r

		# Trim to the left
		snd_data = _trim(snd_data)

		# Trim to the right
		snd_data.reverse()
		snd_data = _trim(snd_data)
		snd_data.reverse()
		return snd_data

	def add_silence(snd_data, seconds):
		#"Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
		r = array('h', [0 for i in xrange(int(seconds*RATE))])
		r.extend(snd_data)
		r.extend([0 for i in xrange(int(seconds*RATE))])
		return r

	def record():
		
		#Record a word or words from the microphone and 
		#return the data as an array of signed shorts.

		#Normalizes the audio, trims silence from the 
		#start and end, and pads with 0.5 seconds of 
		#blank sound to make sure VLC et al can play 
		#it without getting chopped off.
		
		p = pyaudio.PyAudio()
		stream = p.open(format=FORMAT, channels=1, rate=RATE,
			input=True, output=True,
			frames_per_buffer=CHUNK_SIZE)

		num_silent = 0
		snd_started = False

		r = array('h')

		while 1:
			# little endian, signed short
			snd_data = array('h', stream.read(CHUNK_SIZE))
			if byteorder == 'big':
				snd_data.byteswap()
			r.extend(snd_data)

			silent = is_silent(snd_data)

			if silent and snd_started:
				num_silent += 1
			elif not silent and not snd_started:
				snd_started = True

			if snd_started and num_silent > 30:
				break

		sample_width = p.get_sample_size(FORMAT)
		stream.stop_stream()
		stream.close()
		p.terminate()

		r = normalize(r)
		r = trim(r)
		r = add_silence(r, 0.5)
		return sample_width, r
		
	def proces_to_google(path):
		#converteren naar FLAC
		input = audiotools.open(path)

		input.convert((u'%s.flac' % path), 
						audiotools.FlacAudio,
						compression=audiotools.FlacAudio.COMPRESSION_MODES[8],
						progress=progress)	
		path = (u'%s.flac' % path)
		
		#versturen naar google
		f = open(path,'rb')
		flac_cont = f.read()
		f.close()
		
		lang_code='en-US'
		googl_speech_url = 'https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&pfilter=2&lang=%s&maxresults=6'%(lang_code)
		hrs = {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7",'Content-type': 'audio/x-flac; rate=16000'}
		req = urllib2.Request(googl_speech_url, data=flac_cont, headers=hrs)
		p = urllib2.urlopen(req)

		res = eval(p.read())['hypotheses']
		map(os.remove, (path))
		return res

	def record_to_file(path):
		"Records from the microphone and outputs the resulting data to 'path'"
		sample_width, data = record()
		data = pack('<' + ('h'*len(data)), *data)

		wf = wave.open(path, 'wb')
		wf.setnchannels(1)
		wf.setsampwidth(sample_width)
		wf.setframerate(RATE)
		wf.writeframes(data)
		wf.close()
		
		proces_to_google(path)
