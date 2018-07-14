from aip import AipOcr
import time
import json
APP_ID = '11470546'
API_KEY = 'hBYWy8rqaABMrkKCdFpNqOaj'
SECRET_KEY = 'Eox3cFvvj2oV0I6OHqufUt4b7yfdYfyK '
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
filePathc = raw_input("filePath:")
image = get_file_content(filePathc)

result = client.tableRecognitionAsync(image)
print(result)
result  = json.load(str(result))
print (type(result))

for i in range(1,10):
    print(client.getTableRecognitionResult(requestId))
    time.sleep(500)