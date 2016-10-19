
colors = [['hi', 'hi', 'hi'],
          ['ho', 'ho', 'ho']]



def localize(colors):



    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))

    # Matrix size
    print len(colors)     # returns number of rows
    print len(colors[0])  # returns number of columns in row [0]
    print len(colors[1])  # returns number of columns in row [1]

    # Changes type to float
    print type(len(colors))
    print float(len(colors))
    print type(float(len(colors)))

    # Divides 1.0 into as many equal pieces as size of matrix.
    print 1.0 / 2 / 3      # 0.16666
    print 1.0 / (2 * 3)    # 0.16666



    #p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]

    #
    p = [[0,0,0],[0,0,0]]
    for row in range(len(colors[0])):
        p[1] = pinit
        for col in range(len(colors)):
            p[0] = pinit

    print 'FUNC BELOW'
    return p



print localize(colors)


