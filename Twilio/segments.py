def segments(message):
    res = []
    row,start,end = 0,0,154
    if len(message)<=160:
        res.append(message)
        return res
    while end<len(message):
        # if the word in the end of the segment need to be seperate
        # it is better to end on the last word.
        if message[end]!=" ":
            while  message[end]!=" " and message[end+1]!=" ":
                end-=1
            res.append(message[start:end+1])
            row+=1
            start = end+1
            end = start+154
            if message[end]==" ":
                res.append(message[start:end + 1])
                start = end+1
                end = start+154
                row+=1
    res.append(message[start:end + 1])
    row+=1
    for i in range(row):
        res[i]+="("+str(i+1)+"/"+str(row)+")"
    return res
message="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus"
print (segments(message))

