require 'json'

module Jekyll
  class BeerPage < Page
    def initialize(site, base, beer)
      @site = site
      @base = base
      @name = 'index.html'

      slug = beer['beer_name'].downcase.gsub(/[^a-z0-9]+/, '-').gsub(/^-|-$/, '')
      @dir = File.join('beers', slug)

      self.process(@name)
      self.data = {
        'layout'   => 'beer',
        'title'    => beer['beer_name'],
        'beer_name'     => beer['beer_name'],
        'brewery'  => beer['brewery'],
        'details'  => beer['details'],
        'notes'    => beer['notes'],
        'color'    => beer['color'],
        'image'    => beer['image'],
        'slug'     => slug
      }
      self.content = ''
    end
  end

  class BeerPageGenerator < Generator
    safe true

    def generate(site)
      beers = site.data['beers']
      return unless beers

      beers.each do |beer|
        site.pages << BeerPage.new(site, site.source, beer)
      end
    end
  end
end
