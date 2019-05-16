from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from .forms import HeartRate
from .models import Scan
import numpy as np
import math
#import pandas as pd
#import matplotlib.pyplot as plt

# Create your views here.
def home(request):
    return render(request, 'dashboard/base.html')

def user(request):
    return render(request, 'dashboard/user.html')

def scans(request):
    return render(request, 'dashboard/scans.html')

def scanUpload(request):
    if request.method == 'POST':
        form = HeartRate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('scans')

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['urls'] = fs.url(name)
        #print(uploaded_file.name)
        #print(uploaded_file.size)
        #print(context)
    return render(request, 'scans.html', context)

"""def process(request):
    if request.method == 'POST':
        measures = {}
        filename = request.FILES['document']
        def get_data(filename):
            dataset = pd.read_csv(filename)
            return dataset
        def rolmean(dataset, hrw, fs):
            mov_avg = dataset[filename].rolling(int(hrw*fs)).mean()
            avg_hr = (np.mean(dataset.hart))
            mov_avg = [avg_hr if math.isnan(x) else x for x in mov_avg]
            mov_avg = [x*1.2 for x in mov_avg]
            dataset['hart_rollingmean'] = mov_avg
        def detect_peaks(dataset):
            window = []
            peaklist = []
            listpos = 0
            for datapoint in dataset.hart:
                rollingmean = dataset.hart_rollingmean[listpos]
                if (datapoint < rollingmean) and (len(window) < 1):
                    listpos += 1
                elif (datapoint > rollingmean):
                    window.append(datapoint)
                    listpos += 1
                else:
                    maximum = max(window)
                    beatposition = listpos - len(window) + (window.index(max(window)))
                    peaklist.append(beatposition)
                    window = []
                    listpos += 1
            measures['peaklist'] = peaklist
            measures['ybeat'] = [dataset.hart[x] for x in peaklist]
        def calc_RR(dataset, fs):
            RR_list = []
            peaklist = measures['peaklist']
            cnt = 0
            while (cnt < (len(peaklist)-1)):
                RR_interval = (peaklist[cnt+1] - peaklist[cnt])
                ms_dist = ((RR_interval / fs) * 10000.0)
                RR_list.append(ms_dist)
                cnt += 1
            measures['RR_list'] = RR_list
        def calc_bpm():
            RR_list = measures['RR_list']
            measures['bpm'] = 60000 / np.mean(RR_list)
        def plotter(dataset, title):
            peaklist = measures['peaklist']
            ybeat = measures['ybeat']
            plt.title(title)
            plt.plot(dataset.hart, alpha=0.5, color='blue', label="raw signal")
            plt.plot(dataset.hart_rollingmean, color ='green', label="moving average")
            plt.scatter(peaklist, ybeat, color='red', label="average: %.1f BPM" %measures['bpm'])
            plt.legend(loc=4, framealpha=0.6)
            plt.show()
        def process(dataset, hrw, fs): #Remember; hrw was the one-sided window size (we used 0.75) and fs was the sample rate (file is recorded at 100Hz)
            rolmean(dataset, hrw, fs)
            detect_peaks(dataset)
            calc_RR(dataset, fs)
            calc_bpm()
            plotter(dataset, "My Heartbeat Plot")
        def display(dataset):
            dataset = get_data(filename)
            process(dataset, 0.75, 100)
            return process
    return display"""



