assert 'PIRATE' in globals().keys(), 'Is your variable named PIRATE?'
assert '_PARROT' in globals().keys(), 'Is your variable named _PARROT?'
assert 'Ship' in globals().keys(), 'Is your variable named Ship?'
assert Ship==PIRATE+_PARROT or Ship==_PARROT+PIRATE, 'Your variable is not a string. Try again.'
assert type(PIRATE)==str, 'Your variable is not a string. Try again.'
print('Good job!')