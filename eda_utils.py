
import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import os
import seaborn as sns
import numpy as np
from sklearn import metrics
from sklearn.metrics import precision_recall_curve, roc_curve, precision_score



def plot_bars(data: pd.DataFrame, 
                        variables: list,
                        plots_per_row:int =3):

    
    num_plots = len(variables)
    num_rows = int(np.ceil(num_plots/plots_per_row).item()) 
    
    fig, axs = plt.subplots(num_rows, plots_per_row,
                            figsize=(plots_per_row * 4, num_rows * 3),
                            dpi=100)
    axs = axs.ravel()  
    
    for i, variable in enumerate(variables):
        labels = data[variable].value_counts().index
        values =  data[variable].value_counts()
        values =  round(values/sum(values), 2)*100
        
        axs[i].bar(labels, values, width=0.7,color = "teal",
        linewidth = 3,alpha = 0.7
        )
        
        axs[i].set_title(f'{variable}')
        axs[i].set_xlabel(f'{variable}')
        axs[i].set_ylabel(f'Frequnecy (%)')
        axs[i].set_xticks(np.arange(len(labels)))
        axs[i].set_xticklabels(labels, rotation= 70)
        
        
        
        axs[i].grid( linestyle='--', alpha=0.7)
        
    
    for ax in axs[num_plots:]:
        ax.axis('off')
    
    fig.tight_layout(pad=2.0)
    
    plt.show()
    
    
def plot_bar(data: pd.DataFrame, variable: str,
             modalities: list=None, 
             modalities_names=None, 
             modalities_colors: list=None,
             x_ticks_rotation:float=None):
    labels = data[variable].value_counts().index
    values =  data[variable].value_counts()
    values =  values/sum(values)*100
    fig, ax = plt.subplots(figsize =(8,6), dpi = 100)
    ax.bar(labels, values, width=0.7,
        color = modalities_colors,
        edgecolor = "black",
        linewidth = 3,alpha = 0.7
        )
    if modalities:
        ax.set_xticks(modalities)
        ax.set_xticklabels(modalities_names)
    ax.set_xlabel(variable, fontsize = 15)
    ax.set_ylabel("Frequency(%)", fontsize = 15)
    plt.xticks(fontsize=12, rotation=x_ticks_rotation)
    plt.yticks(fontsize=12)
    plt.show();


def plot_histograms(data: pd.DataFrame, 
                         variables: list,
                         plots_per_row:int =3):

    
    num_plots = len(variables)
    num_rows = int(np.ceil(num_plots/plots_per_row).item()) 
    
    fig, axs = plt.subplots(num_rows, plots_per_row,
                            figsize=(plots_per_row * 4, num_rows * 3),
                            dpi=100)
    axs = axs.ravel()  
    
    for i, variable in enumerate(variables):
        
        
        axs[i].hist(data[variable], alpha=0.7, color='teal')
        axs[i].set_title(f'{variable}')
        axs[i].set_xlabel(f'{variable}')
        axs[i].set_ylabel(f'Frequnecy')
        
        axs[i].grid( linestyle='--', alpha=0.7)
        
    
    for ax in axs[num_plots:]:
        ax.axis('off')
    
    fig.tight_layout(pad=2.0)
    
    plt.show()

def plot_target_vs_num_feature(data: pd.DataFrame, 
                               feature: str, target:str="Risk",
                               num_bins:int=10):
    plt.figure(figsize=(10,7))
    sns.histplot(data, x=feature, hue=target, alpha=0.2, bins=num_bins, stat="frequency")
    plt.title(f"{feature} Vs {target}")
    plt.grid( linestyle='--', alpha=1)
    plt.show()
    

def binary_plot_count(data:pd.DataFrame, categorical_feats:list, 
                      target:str="Risk", plots_per_row:int=3):
    
    num_plots = len(categorical_feats)
    num_rows = int(np.ceil(num_plots/plots_per_row).item()) 
    
    fig, axs = plt.subplots(num_rows, plots_per_row,
                            figsize=(plots_per_row * 4, num_rows * 3),
                            dpi=100)
    axs = axs.ravel()  
    
    for i, variable in enumerate(categorical_feats):
        
        sns.countplot(data=data, x=variable, ax=axs[i], palette='crest', hue=target, stat="proportion")
        axs[i].set_title(f'{variable} Distribution', size = 14)
        axs[i].set_xlabel(None)
        axs[i].tick_params(axis='x', rotation=70)
        
    for ax in axs[num_plots:]:
        ax.axis('off')   
    plt.tight_layout()
    
    plt.show()

def has_outliers(data:pd.DataFrame, feature:str):
    # Calculate the upper and lower limits
    Q1 = data[feature].quantile(0.25)
    Q3 = data[feature].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR

    # Create arrays of Boolean values indicating the outlier rows
    upper_array = np.where(data[feature] >= upper)[0]
    lower_array = np.where(data[feature] <= lower)[0]

    num_outliers = len(upper_array) + len(lower_array)

    return num_outliers, lower_array, upper_array, Q1, Q3

def replace_outliers(data:pd.DataFrame, outlier_feature:str):
    _, lower_array, upper_array, Q1, Q3=has_outliers(data, outlier_feature)
    data.loc[lower_array, outlier_feature] = Q1
    data.loc[upper_array, outlier_feature] = Q3
    return data


     
def plot_ROC_curve(clf, label_leg, X, y_obs, class_index):

  fig, ax = plt.subplots(figsize=(6,6))

  # Luck line
  ax.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--", label = label_leg[0])

  # Get proba predictions:
  y_scores = clf.predict_proba(X)

  # Getting the ROC curve values
  fpr = dict() ; tpr = dict()

  fpr, tpr, _ = roc_curve(y_obs, y_scores[:,1], pos_label=class_index)

  ax.plot(fpr, tpr, color="navy", lw=2, linestyle="-", label=label_leg[1])

  ax.set_xlim([0, 1])
  ax.grid(color='grey', linestyle='--', linewidth=1)
  ax.set_xlabel("False Positive Rate")
  ax.set_ylabel("True Positive Rate")
  ax.set_title("ROC curve", pad=20)

  ax.legend(fontsize=12, bbox_to_anchor=(1.04, 0.5), loc="center left", frameon=False, title = "Models", title_fontsize=20)
  plt.show()
  
  
def print_metrics(clf, X, y_obs, printCM=False, title="Classifier Performance"):

    y_preds = clf.predict(X)
    cm= metrics.confusion_matrix(y_obs, y_preds)
    TN, FP, FN, TP = cm.flatten()
    acc = (TP+TN)/(sum(cm.flatten()))
    TPR = TP/(TP+FN)
    TNR= TN/(TN+FP)
    FPR= FP/(FP+TN)


    print(f"\n{title}\n")
    print(f"Accuracy: {acc:.3f}")
    print(f"     TPR: {TPR:.3f}")
    print(f"     TNR: {TNR:.3f}")
    print(f"     FPR: {FPR:.3f}")

    if printCM:
        disp = metrics.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['good', 'bad'])
        disp.plot()
        plt.show()



