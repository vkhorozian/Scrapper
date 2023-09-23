
# SCRIPT PART 1


<br>

### Link example: https://www.superpages.com/search?search_terms=general+contractors&geo_location_terms=07657

<br>



---
### Request this site then look for this in the html that was just pulled down

```
<a class="weblink-button" href="http://johansengeneralcontracting.com" rel="nofollow noopener" target="_blank" </a>

grep :  href="http://johansengeneralcontracting.com"
```


Create a list of all the links that are found in the html

```python
# create a list of all the links that are found in the html
links = soup.find_all('a', class_='weblink-button')
```

### Loop through the list of links and extract the URL embedded into href tag

```python
# Loop through the list of links and extract the URL embedded into href tag
for link in links:
    print(link['href'])
```





















## Extract the URL embedded into href tag and do a new Request on that new link

```

<a href="mailto:servpro9280@optonline.net">servpro9280@optonline.net</a>

```



