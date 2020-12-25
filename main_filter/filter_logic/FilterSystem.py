class FilterSystem:
    
    def Quality(object, acousticness, danceability, energy, instrumental, liveness, loudness, speechiness, tempo, valence):
        quality = 0.0
        if acousticness == "Low":
            quality = -(object.getAcousticness()/0.996)
        elif acousticness == "High":
            quality = (object.getAcousticness()/0.996)

        if danceability == "Low":
            quality -= (object.getDanceability()/0.988)
		elif danceability == "High":
            quality += (object.getDanceability()/0.988)
		
		if energy == "Low":
            quality -= (object.getEnergy())
		elif energy == "High":
            quality += (object.getEnergy());
		
		if instrumental == "Low":
            quality -= (object.getInstrumental());
		elif instrumental == "High":
            quality += (object.getInstrumental());
		
		if liveness == "Low":
            quality -= (object.getLiveness());
		elif liveness == "High":
            quality += (object.getLiveness());
		
		if loudness == "Low":
            quality -= (object.getLoudness()/3.744);
		elif loudness == "High":
            quality += (object.getLoudness()/3.744);
		
		if speechiness == "Low":
            quality -= (object.getSpeechiness()/0.968);
		elif speechiness == "High":
            quality += (object.getSpeechiness()/0.968);
		
		if tempo == "Low":
            quality -= (object.getTempo()/247.824);
		elif tempo == "High":
            quality += (object.getTempo()/247.824);
		
		if valence == "Low":
            quality -= (object.getValence());
		elif valence == "High":
            quality += (object.getValence());
		
		return ((quality/9)*100); 
