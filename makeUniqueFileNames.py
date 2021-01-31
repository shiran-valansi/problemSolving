def getFolderNames(names):
    """
    Given an array of strings names of size n. You will create n folders in your file system such that, at the ith minute, you will create a folder with the name names[i].

    Since two files cannot have the same name, if you enter a folder name which is previously used, the system will have a suffix addition to its name in the form of (k), where, k is the smallest positive integer such that the obtained name remains unique.

    Return an array of strings of length n where ans[i] is the actual name the system will assign to the ith folder when you create it.

    >>> getFolderNames(["pes","fifa","gta","pes(2019)"])
    ['pes', 'fifa', 'gta', 'pes(2019)']


    >>> getFolderNames(["gta","gta(1)","gta","avalon"])
    ['gta', 'gta(1)', 'gta(2)', 'avalon']

    >>> getFolderNames(["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"])
    ['onepiece', 'onepiece(1)', 'onepiece(2)', 'onepiece(3)', 'onepiece(4)']

    >>> getFolderNames(["kaido","kaido(1)","kaido","kaido(1)"])
    ['kaido', 'kaido(1)', 'kaido(2)', 'kaido(1)(1)']

    """
    uniques = {}
    
    for name in names:
        if name in uniques:
            uniques[name] += 1
            count = uniques[name]
            new_name = name + "(" + str(count) +")"
            while new_name in uniques:
                uniques[name] += 1
                count = uniques[name]
                new_name = name + "(" + str(count) + ")"
            uniques[new_name] = 0
        else:    
            uniques[name] = 0
            
    return list(uniques.keys())

if __name__ == "__main__":
    import doctest
    doctest.testmod()