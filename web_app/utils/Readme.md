## Usage:

------------
```python
#
import web_app.utils.MLModel
tr = MLModel.Transformer()
# open the pickle file and load model
with open("path/to/pickle", 'rb') as fp:
    model = pickle.load(fp)
negative = ['negative']
ignore = ['index','id']
user_transformed = tr.transform(pd.dataframe({'name':str,
                                              'race':str,
                                              'flavors':list,
                                              'negative':list
                                              'positive':list,
                                              'medical':list,
                                              'description':str,
                                              }),
                                negative,
                                ignore)
pred = model.predict(user_transformed)
pred[1]
```
```python
Output:
[['#', '#', '#', '#', '#']]
```

<h2>The numbers correspond to the index of the strains in the database</h2>
<div>
    <p>
        the `ignore` keyword is a list of column names that should be excluded from the model.
        the `negative` keyword is a list of column names that should have a negative effect
        on the recommendation, for inital training we used:
    </p>
</div>
<a href="../../README.md">Main Readme</a>