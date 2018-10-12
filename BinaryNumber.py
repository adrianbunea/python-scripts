number = input('Input your number:')

if(len(number) == 1):
	exit('FAIL: String length is 1, it cannot be binary')
	
for x in range(0, len(number)-1):
	if number[x] != '1' and number[x] != '0':
		exit('FAIL: Number does not contain just 0s and 1s')
		
if number[len(number)-1] != 'b':
	exit('FAIL: String doesn\'t end with \'b\'')
	
print('Number is binary!')