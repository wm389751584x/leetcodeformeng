from collections import defaultdict
ice_cream = defaultdict(lambda: False)

ice_cream['Sarah'] = True
ice_cream['Abdul'] = True

print(ice_cream['Sarah'])
# >>>Chunky Monkey

print(ice_cream['Joe'])
# >>>Vanilla