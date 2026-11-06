import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score
DF = pd.read_csv('heart.csv')
# print(DF.head())
def z_thal(randomness):
    data = DF.drop(columns=['target'])
    target = DF['target']

    # randomness = int(input())

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.2, random_state = randomness)
    model = RandomForestClassifier(random_state=randomness)
    model.fit(data_train, target_train)
    target_prediction = model.predict(data_test)

    accuracy = accuracy_score(target_test, target_prediction)
    recall = recall_score(target_test, target_prediction)

    # print("recall_thal = " + str(recall))
    # print("accuracy_thal = " + str(accuracy))
    return accuracy, recall

def bez_thal(randomness):
    data = DF.drop(columns=['target', 'thal'])
    target = DF['target']
    # print("Kolumny drugiego modelu:", data.columns)
    data_train_b, data_test_b, target_train_b, target_test_b = train_test_split(data, target, test_size = 0.2, random_state = randomness)
    model_b = RandomForestClassifier(random_state=randomness)
    model_b.fit(data_train_b, target_train_b)
    target_prediction_b = model_b.predict(data_test_b)

    accuracy_b = accuracy_score(target_test_b, target_prediction_b)
    recall_b = recall_score(target_test_b, target_prediction_b)

    # print("recall = " + str(recall_b))
    # print("accuracy = " + str(accuracy_b))
    return accuracy_b, recall_b
maxi_a = -20
maxi_r = -20
licznik = 0
hip = -20
for i in range (1, 1000):
    a, b = z_thal(i)
    c, d = bez_thal(i)
    maxi_a = max(maxi_a, a - c) 
    maxi_r = max(maxi_r, b - d)
    # print (str(i))
    # Gdy zasymulowałem uczenie się modelu to zauważyłem że za bardzo nie spada accuracy i recall po 
    # usunięciu kolmuny thal. Więc sprawdzam powyżej jaka jest największa różnica między accuracy 
    # z i bez kolumny thal. Tak samo sprawdzam maksymalną różnicę recall
    hip = max(b - a, hip)
    if (b - a > 0.05):              
        licznik += 1
    # tutaj ^ sprawdzam hipotezę 2 tzn. czy recall będzie większy od accuracy o co najmniej 5%

print(maxi_a)
print(maxi_r)
print(hip)
print(licznik)
# poniżej wartości dla i od 1 do 1000
# 0.029268292682926855
# 0.03260869565217395
# 0.039024390243902474
# 0

# pierwsza hipoteza obalona - największa różnica między accuracies to tylko 0.029 co jest znacznie mniejsze
# od przypuszaczanego 0.1

# druga hipoteza też obalona - największa różnica między recall i accuracy to 0.039, a nie zakładane 0.05