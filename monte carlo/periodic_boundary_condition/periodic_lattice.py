import numpy as np

class Periodic_Lattice(np.ndarray):

    def __new__(cls, input_array, lattice_spacing=1.):
        obj = np.asarray(input_array).view(cls)
        
        obj.lattice_shape = input_array.shape
        obj.lattice_dim = len(input_array.shape)
        obj.lattice_spacing = lattice_spacing

        return obj
    
    def __getitem__(self, index):
        index = self.latticeWrapIdx(index)
        return super(Periodic_Lattice, self).__getitem__(index)
    
    def __setitem__(self, index, item):
        index = self.latticeWrapIdx(index)
        return super(Periodic_Lattice, self).__setitem__(index, item)
    
    def __array_finalize__(self, obj):

        if obj is None: return
            
        try: 
            self.lattice_shape   = getattr(obj, 'lattice_shape', obj.shape)
            self.lattice_dim     = getattr(obj, 'lattice_dim', len(obj.shape)) 
            self.lattice_spacing = getattr(obj, 'lattice_spacing', None)
        except: 
            self.lattice_shape   = obj.shape
            self.lattice_dim     = len(self.lattice_shape)
            self.lattice_spacing = None
        pass
    
    def latticeWrapIdx(self, index):
        if hasattr(index, '__iter__') and len(index)>1:
            if len(index) != len(self.lattice_shape): return index  
            if any(type(i) == slice for i in index): return index   
        else:
            if self.lattice_dim == 1: index = [index]
            else:  return index
        try:
            if len(index) == self.lattice_dim: 
                mod_index = tuple(( (i%s + s)%s for i,s in zip(index, self.lattice_shape)))
                return mod_index
        except:
            raise ValueError('Unexpected index: {}'.format(index))


if __name__=='__main__':
    arr = np.array([[ 11.,  12.,  13.,  14.],
                    [ 21.,  22.,  23.,  24.],
                    [ 31.,  32.,  33.,  34.],
                    [ 41.,  42.,  43.,  44.]])
    test_vals = [[(1,1), 22.], [(3,3), 44.], [( 4, 4), 11.], # [index, expected value]
                [(3,4), 41.], [(4,3), 14.], [(10,10), 33.]]

    periodic_arr  = Periodic_Lattice(arr)
    passed = (periodic_arr == arr).all()
    passed *= all([periodic_arr[idx] == act for idx, act in test_vals])
    print("Iterating test values. Result: {}".format(passed))