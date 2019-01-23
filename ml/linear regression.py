# based on equations from artificial intellegence: a modern appoarch page 719

data  = [1,2,3,4,5,6,7,8]
label = [1,2,3,4,5,6,7,8]

a = len(data)*sum( data[i]*label[i] for i in range(len(data)))
b = sum(data)*sum(label)
c = len(data)*sum(x**2 for x in data)
d = sum(data)**2
w1 = (a-b)/(c-d)

w0 = sum(y-w1*sum(data) for y in label)/len(data)

print(w1, w0)