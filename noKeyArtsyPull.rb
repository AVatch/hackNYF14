require 'json'
require 'hyperclient'
require 'simple_http'
require 'httparty'
require 'open-uri'
require 'searchbing'

artistsAndWorks = [
	
	{	
		:artistID => '4d8b92b64eb68a1b2c000414',
		:artworkID => '4d8b92eb4eb68a1b2c000968'
	},
	
	{
	    :artistID => '4d8b92944eb68a1b2c000264',
	    :artworkID => '532886440bb6d6e860000151'
	},
	
	{
		:artistID => '4d8b92684eb68a1b2c00009e',
		:artworkID => '4d8b937c4eb68a1b2c001722'
	},

	{
		:artistID => '4d8b927e4eb68a1b2c000168',
		:artworkID => '4d8b93b04eb68a1b2c001b9d'
	},
	
	{ 
		:artistID => '4d8b92b44eb68a1b2c0003fe',
		:artworkID => '4d8b92ee4eb68a1b2c0009ab'
	},

	{
		:artistID => '4d8b929c4eb68a1b2c0002e2',
		:artworkID => '4d8b93394eb68a1b2c0010fa'
	},

	{
		:artistID => '4d8b92774eb68a1b2c000134',
		:artworkID => '4eb864d292f64f0001011a57'
	}

]

xapp_token = 'ARTSY APP TOKEN'

API = Hyperclient.new('https://api.artsy.net/api').tap do |api|
  api.headers.update('Accept' => 'application/vnd.artsy-v2+json')
  api.headers.update('X-Xapp-Token' => xapp_token)
end

def convURL(url)
	newURL = url.sub('medium', "large")
	return newURL
end

def nytimes(concept) 
      url = URI.encode("http://api.nytimes.com/svc/search/v2/articlesearch.json?q=#{concept}&page=2&api-key=NYTIMEKEY")
      response = HTTParty.get(url)
      articles = []
      response["response"]["docs"].each do |article|
           articles << {:url => article["web_url"], :name => article["headline"]["main"], :description=> article["lead_paragraph"]}
      end
     articles[0..5]
end

def searchBing(term)
	bing_image = Bing.new('RyQOk5Q+193abiM+CB4eKNs3jYFYVJLS5+NIfkNutRA',1,'Image')
	bing_result = bing_image.search(term + "self portrait")
	return bing_result[0][:Image][0][:MediaUrl]
end

def createArtHash(artistID, artworkID)
	artist = API.artist(id: artistID)
	puts "#{artist.name} was born on #{artist.birthday} in #{artist.hometown}."
	puts "#{artist.blurb}"
	artwork = API.artwork(id: artworkID)
	puts "#{artwork.title} was made in #{artwork.date}"

	art_hash = Hash.new 
	art_hash[:artist] = artist.name # pre defined
	art_hash[:art_title] = artwork.title # from artsy
	art_hash[:art_pic_url] = convURL(artwork[:_links][:thumbnail].to_s) # from artsy
	art_hash[:artist_bio] = artist.blurb # from artsy
	art_hash[:artist_pic_url] = searchBing(artist.name) # from bing
	art_hash[:articles] = nytimes(artist.name.to_s.sub(' ', '+')) # from NYTimes
	return art_hash
end

def createGalleryArray(artistsAndWorks)
	galleryArrayOfArt = []
	for artistWork in artistsAndWorks
		galleryArrayOfArt.push(createArtHash(artistWork[:artistID], artistWork[:artworkID]))
	end
	return galleryArrayOfArt
end


galleryOfArt = createGalleryArray(artistsAndWorks)

# puts galleryOfArt

artJSON = JSON.generate(galleryOfArt)

print JSON.pretty_generate(galleryOfArt)

File.open("art.json", "w") do |f|
	f.write(artJSON)
end

# puts art_hash[:artist]
# puts art_hash[:art_title]
# puts art_hash[:art_pic_url]
# puts art_hash[:artist_bio]
# puts art_hash[:artist_pic_url]
# puts art_hash[:articles]