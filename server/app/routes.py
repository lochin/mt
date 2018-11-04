from app import app
from flask import jsonify, request
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import operator

uza = load_files('.\\uza')

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(uza.data)
clf = MultinomialNB().fit(X_train_counts, uza.target)
categories = uza.target_names


@app.route('/', methods=['POST'])
def index():
    global count_vect, clf, categories
    
    content = request.get_json()    
    text = content.get('content')       

    X_new_counts = count_vect.transform([text])    
    proba = clf.predict_proba(X_new_counts)
    norm = [float(i)/sum(proba[0]) for i in proba[0]]    
    p_dict = dict(zip(categories, norm))
    sorted_dic = sorted(p_dict.items(), key=operator.itemgetter(1), reverse=True)
    return jsonify(labels=categories, data=norm, dict=sorted_dic)