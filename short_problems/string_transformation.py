def transform(in_,out_):
    # transform an array in another array, one element at a time
    [print(out_[:ind] + x + in_[ind+1:]) for ind,x in enumerate(in_) if in_[ind] != out_[ind]]
    print(out_)

transform("floor", "brake")
transform("wood", "book")
