from os import listdir

class Library():

    def __init__(self, home_dir, library_path, galleries):

        # build library
        lib = dict()
        for gal_name in galleries:
            path = library_path + gal_name + '/'
            gal_items = dict()
            for f in sorted(listdir(home_dir + path), reverse=True):
                # ignore everything but jpg and txt
                if '.jpg' not in f and '.txt' not in f:
                    continue

                name = f.split('.')[0]
                if name not in gal_items:
                    gal_items[name] = dict()
                    gal_items[name]['path'] = None
                    gal_items[name]['title'] = None
                    gal_items[name]['data'] = None

                if '.jpg' in f:
                    gal_items[name]['path'] = path + f
                    continue

                # parse txt
                reading = open(home_dir + path + f, 'r')
                lines = reading.read()
                reading.close()
                lines = lines.split('-')
                if len(lines) != 2:
                    continue

                gal_items[name]['title'] = lines[0]
                gal_items[name]['data'] = lines[1]


            lib[gal_name] = gal_items

        self._libraries = lib


    @property
    def libraries(self):
        return self._libraries
