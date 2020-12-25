class Graph:

    def __init__(self, song_list):
        self.node_list = song_list
        self.avg_acousticness = 0.0
        self.avg_dancebility = 0.0
        self.avg_energy = 0.0
        self.avg_instrumental = 0.0
        self.avg_liveness = 0.0
        self.avg_loudness = 0.0
        self.avg_mode = 0.0
        self.avg_speechiness = 0.0
        self.avg_tempo = 0.0
        self.avg_valence = 0.0

    def link(self):
        for i in range(0, len(self.node_list - 1)):
            self.node_list[i].addAdj(self.node_list[i+1])

    def setAvgAcousticness():
		total = 0.0
		num_song = 0
		cur_node = node_list[0]
		while !cur_node.adjlist.empty(): #check whether the empty() will work or not
			total += cur_node.song.getAcousticness()
			cur_node = cur_node.adjlist[0]
			num_song++
		self.avg_acousticness = total/num_song
	
	
	##
	# Returns the average acousticness quality in the graph, going through the each node/songObject in the list
	# @return a double value
	#
	def getAvgAcousticness(): 
		if self.avg_acousticness == 0.0:
			self.setAvgAcousticness()
		return self.avg_acousticness
	
    def setAvgDanceability():
		total = 0.0
		num_song = 0
		cur_node = node_list[0]
		while !cur_node.adjlist.empty(): #check whether the empty() will work or not
			total += cur_node.song.getDanceability()
			cur_node = cur_node.adjlist[0]
			num_song++
		self.avg_dancebility = total/num_song
	
	
	##
	# Returns the average acousticness quality in the graph, going through the each node/songObject in the list
	# @return a double value
	#
	def getAvgDanceability(): 
		if self.avg_dancebility == 0.0:
			self.setAvgDanceability()
		return self.avg_dancebility
	
    def setAvgEnergy():
		total = 0.0
		num_song = 0
		cur_node = node_list[0]
		while !cur_node.adjlist.empty(): #check whether the empty() will work or not
			total += cur_node.song.getEnergy()
			cur_node = cur_node.adjlist[0]
			num_song++
		self.avg_energy = total/num_song
	
	
	##
	# Returns the average acousticness quality in the graph, going through the each node/songObject in the list
	# @return a double value
	#
	def getAvgEnegry(): 
		if self.avg_energy == 0.0:
			self.setAvgEnergy()
		return self.avg_energy
	
    def setAvgInstrumental():
		total = 0.0
		num_song = 0
		cur_node = node_list[0]
		while !cur_node.adjlist.empty(): #check whether the empty() will work or not
			total += cur_node.song.getInstrumental()
			cur_node = cur_node.adjlist[0]
			num_song++
		self.avg_instrumental = total/num_song
	
	
	##
	# Returns the average acousticness quality in the graph, going through the each node/songObject in the list
	# @return a double value
	#
	def getAvgInstrumental(): 
		if self.avg_instrumental == 0.0:
			self.setAvgInstrumental()
		return self.avg_instrumental
	
    def setAvgLiveness():
		total = 0.0
		num_song = 0
		cur_node = node_list[0]
		while !cur_node.adjlist.empty(): #check whether the empty() will work or not
			total += cur_node.song.getLiveness()
			cur_node = cur_node.adjlist[0]
			num_song++
		self.avg_liveness = total/num_song
	
	
	##
	# Returns the average acousticness quality in the graph, going through the each node/songObject in the list
	# @return a double value
	#
	def getAvgLiveness(): 
		if self.avg_liveness == 0.0:
			self.setAvgLiveness()
		return self.avg_liveness
	
    def setAvgLoudness():
		total = 0.0
		num_song = 0
		cur_node = node_list[0]
		while !cur_node.adjlist.empty(): #check whether the empty() will work or not
			total += cur_node.song.getLoudness()
			cur_node = cur_node.adjlist[0]
			num_song++
		self.avg_loudness = total/num_song
	
	
	##
	# Returns the average acousticness quality in the graph, going through the each node/songObject in the list
	# @return a double value
	#
	def getAvgLoudness(): 
		if self.avg_loudness == 0.0:
			self.setAvgLoudness()
		return self.avg_loudness
	
    def setAvgMode():
		total = 0.0
		num_song = 0
		cur_node = node_list[0]
		while !cur_node.adjlist.empty(): #check whether the empty() will work or not
			total += cur_node.song.getMode()
			cur_node = cur_node.adjlist[0]
			num_song++
		self.avg_mode = total/num_song
	
	
	##
	# Returns the average acousticness quality in the graph, going through the each node/songObject in the list
	# @return a double value
	#
	def getAvgMode(): 
		if self.avg_mode == 0.0:
			self.setAvgMode()
		return self.avg_mode
	
    def setAvgSpeechiness():
		total = 0.0
		num_song = 0
		cur_node = node_list[0]
		while !cur_node.adjlist.empty(): #check whether the empty() will work or not
			total += cur_node.song.getSpeechiness()
			cur_node = cur_node.adjlist[0]
			num_song++
		self.avg_speechiness = total/num_song
	
	
	##
	# Returns the average acousticness quality in the graph, going through the each node/songObject in the list
	# @return a double value
	#
	def getAvgSpeechiness(): 
		if self.avg_speechiness == 0.0:
			self.setAvgSpeechiness()
		return self.avg_speechiness
	
    def setAvgTempo():
		total = 0.0
		num_song = 0
		cur_node = node_list[0]
		while !cur_node.adjlist.empty(): #check whether the empty() will work or not
			total += cur_node.song.getTempo()
			cur_node = cur_node.adjlist[0]
			num_song++
		self.avg_tempo = total/num_song
	
	
	##
	# Returns the average acousticness quality in the graph, going through the each node/songObject in the list
	# @return a double value
	#
	def getAvgTempo(): 
		if self.avg_tempo == 0.0:
			self.setAvgTempo()
		return self.avg_tempo
	
    def setAvgValance():
		total = 0.0
		num_song = 0
		cur_node = node_list[0]
		while !cur_node.adjlist.empty(): #check whether the empty() will work or not
			total += cur_node.song.getValance()
			cur_node = cur_node.adjlist[0]
			num_song++
		self.avg_valence = total/num_song
	
	
	##
	# Returns the average acousticness quality in the graph, going through the each node/songObject in the list
	# @return a double value
	#
	def getAvgValance(): 
		if self.avg_valence == 0.0:
			self.setAvgValance()
		return self.avg_valence
