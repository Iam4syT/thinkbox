from solution import handler
import json
for reading, expected in [(0,200),(450,200),(-1,400),(True,400),('450',400),(None,400)]:
    assert handler({'body':json.dumps({'irradiance':reading})})['statusCode'] == expected
assert handler({'body':'{'})['statusCode'] == 400
print('7 forecast request checks passed')
