ip = input("Please enter an IP address: ")

if ip[-1] != '.':
    ip += '.'
    
segment = 1
segmentLength = 0
# char = ''

for char in ip:
    if char == '.':
        print("Segment {} contains {} characters.".format(segment, segmentLength))
        segment += 1
        segmentLength = 0

    else:
        segmentLength += 1

# if char != '.':
#         print("Segment {} contains {} characters.".format(segment, segmentLength))
