from django.shortcuts import render,HttpResponse

# Create your views here.

import pickle

model_file_path = 'static/rfe_KNN.pkl'
with open(model_file_path, 'rb') as f:
    knn_model = pickle.load(f)





def index(request):

    if request.method == "POST":
        HTN=int(request.POST.get('HTN_1'))
        Typical_Chest_Pain_1=int(request.POST.get('Typical_Chest_Pain_1'))
        Atypical=int(request.POST.get('Atypical_1'))
        Age=int(request.POST.get('Age'))
        Weight=int(request.POST.get('Weight'))
        BMI=int(request.POST.get('BMI'))
        BP=int(request.POST.get('BP'))
        FBS=int(request.POST.get('FBS'))
        CR=int(request.POST.get('CR'))
        TG=int(request.POST.get('TG'))
        LDL=int(request.POST.get('LDL'))
        HDL=int(request.POST.get('HDL'))
        ESR=int(request.POST.get('ESR'))
        HB=int(request.POST.get('HB'))
        K=int(request.POST.get('K'))
        WBC=int(request.POST.get('WBC'))
        Lymph=int(request.POST.get('Lymph'))
        PLT=int(request.POST.get('PLT'))
        EF_TTE=int(request.POST.get('EF_TTE'))
        Region_RWMA=int(request.POST.get('Region_RWMA'))

        classifier=request.POST.get('classifier')

        print(classifier)

        if classifier=='KNN':
            print("in knn")
            model_file_path = 'static/rfe_KNN.pkl'
            with open(model_file_path, 'rb') as f:
                knn_model = pickle.load(f)
            pred= knn_model.predict([[HTN, Typical_Chest_Pain_1, Atypical, Age, Weight, BMI, BP, FBS, CR, TG, LDL, HDL, ESR, HB, K, WBC, Lymph, PLT, EF_TTE, Region_RWMA]])
        elif classifier=="SVM":
            model_file_path = 'static/rfe_svm.pkl'
            with open(model_file_path, 'rb') as f:
                svm_model = pickle.load(f)
            pred= svm_model.predict([[HTN, Typical_Chest_Pain_1, Atypical, Age, Weight, BMI, BP, FBS, CR, TG, LDL, HDL, ESR, HB, K, WBC, Lymph, PLT, EF_TTE, Region_RWMA]])

        elif classifier=="RF":
            model_file_path = 'static/rfe_rf.pkl'
            with open(model_file_path, 'rb') as f:
                rf_model = pickle.load(f)
            pred= rf_model.predict([[HTN, Typical_Chest_Pain_1, Atypical, Age, Weight, BMI, BP, FBS, CR, TG, LDL, HDL, ESR, HB, K, WBC, Lymph, PLT, EF_TTE, Region_RWMA]])

        else:
            pred="INVALID"


        result=""
        if pred==1:
            result="CAD Detected"
        else:
            result="No CAD detected"

        output={
            "output":result
        }

        print(pred)

        return render(request, "index.html",output)

    else:
        return render(request, "index.html")


