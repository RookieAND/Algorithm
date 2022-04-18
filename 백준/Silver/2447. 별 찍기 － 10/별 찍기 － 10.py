def make_stars(n):
  if n == 1:
    return ['*']

  stars = make_stars(n//3)
  star_list = []

  for star in stars:
    star_list.append(star*3)
  for star in stars:
    star_list.append(star+' '*(n // 3)+star)
  for star in stars:
    star_list.append(star*3)

  return star_list

n = int(input())
print('\n'.join(make_stars(n)))