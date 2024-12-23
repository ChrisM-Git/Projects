# Christopher Martin 
# This is the main python file for flask output to an html page for a lab that outputs model classification results baed on image dstection

from flask import Flask, render_template, request
from train import *


app = Flask(__name__)


lenfile = len(X)
lenlabel = len(labels)


lenvars = f"Number of filenames: {lenfile} Number of labels: {lenlabel}"

validation = """With these two data points, we can create a validation set. The Id is the filename of the dog image and the breed is the label of the dog.
                        We want to validate the two so our model can have accurate predictions. Lets take a closer look at our label column. Below is
                        a total count of images per breed uploaded from our customers and imported to the CSV file.
                        """
valuedesc = """ Look at the total number of dog breed counts above. Some breeds have more images then others.
                            How many images does our model need to learn about the type of breed? It is recommended to have 100
                            annotations of a class for model prediction. Some of our breeds have less, which means our model may
                            not be able to predict certain dog breeds with a high percentage of accuracy, for example, the eskimo dog has 66 images"""

arrayresult = """ With our breed data now in a list, we can easily put that into a variable for future use. Recall we have our ID column from the CSV which represents filenames. 
                  In the next step compare the values in the list with the image filenames to make sure our validation is accurate. To do this, we will split our data
                  into two variables, x and y. x will be our filenames, and y will be the labels. For example, x = filenames y = labels. See the boxes below, define an x and y variable! """

variabledesc = """A note about validation, so far we have extracted data from a CSV file, and assigned ID and Breed to variables filenames and labels. This provides a method
                  for verifying our data. If we skip this step, our models could fail, and results will be inconsistent. Labelling and validation plays an important part to  the success of AI."""

lenresult = """ Great our numbers match! We have 10222 Filenames and labels, thats allot of data! This is where hardware sizing requirements can be a factor when running experiments! The amount of GPU's, storage needed is going to
                be based on how much data we ingest and train. When we do model training in the next section  we will use a quantity of 1000 for our filenames and labels to minimize the time between experiments so we can adjust our models quicker!
                This applies to any generative AI use case, images, text, documents, etc"""
@app.route('/')
def index():
    return render_template("datasci2.html")

@app.route('/', methods=['GET', 'POST'])
def homeform():
    if request.form['action'] == 'data':
        data1 = request.form.get("data1").lower()
        data2 = request.form.get("data2").lower()


        if data1 == "id" and data2 == "breed" or data1 == "breed" and data2 == "id":
           data_answer = f"You entered {data1} and {data2}, that's correct!"
           return render_template("datasci2.html", data_answer=data_answer, validation=validation, valuecount=valuecount, valuedesc=valuedesc)
        else:
           data_answer = "No, that is not correct. The correct answer is id and breed"
           return render_template("datasci2.html", wdata_answer=data_answer, validation=validation,valuecount=valuecount, valuedesc=valuedesc)

    if request.form['action'] == 'arraybutton':
        file1 = request.form.get("file1")
        array1 = request.form.get("array1")
        if array1 == 'labeldata=labels["breed"].to_numpy()' and file1 == 'filenames=["/Users/chrimar3/projects/sample-project/dogbreeds/data/train/" + fname + ".jpg" for fname in labeldata["id"]]':
           array_answer = "You entered the correct syntex, look at the output below, this is a truncated LIST of our filenames and dog breeds (labels) that was collected from the CSV file"
           return render_template("datasci2.html", validation=validation, valuecount=valuecount, valuedesc=valuedesc,array_answer=array_answer, fileresult=filenames20, array=labeldata20, arrayresult=arrayresult)
        else:
            array_answer = f'Inocrrect syntax entered, check your input, and try again!'
            return render_template("datasci2.html", validation=validation, valuecount=valuecount, warray_answer=array_answer)
    if request.form['action'] == 'varbutton':
        varf = request.form.get("varf").lower()
        varl = request.form.get("varl").lower()
        if varf == "f=filenames" and varl == "l=labels":
            variables = f" You entered {varf}  and {varl} for your variables, great job! This will help in understanding validation in the next steps!"
            return render_template("datasci2.html",validation=validation, valuecount=valuecount, valuedesc=valuedesc, fileresult=filenames20, array=labeldata20, arrayresult=arrayresult, variables=variables, variabledesc=variabledesc)
        else:
            novariables = f" You entered {varf}  and {varl} for your variables, please use f=filenames and l=labels for your variables"
            return render_template("datasci2.html",novariables=novariables)
    if request.form['action'] == 'lenbutton':
        formfile = request.form.get("lenfile").lower()
        formlabel = request.form.get("lenlabel").lower()
        if formfile == "len(f)" and formlabel == "len(l)":
            return render_template("datasci2.html", validation=validation, valuecount=valuecount, valuedesc=valuedesc, fileresult=filenames20, array=labeldata20, arrayresult=arrayresult, variabledesc=variabledesc, lenvars=lenvars, lenresult=lenresult)
        else:
            wronganswer = "Incorrect syntax entered,review the previous step to determine the right variables for the len() command"
            return render_template("datasci2.html", wlenvars=wronganswer)

    if request.form['action'] == 'triviabutton':
        guess = int(request.form.get("triviaq"))
        if guess > int(qtybreeds):

            toohigh = "Your guess is too high, try a lower number!"
            return render_template("datasci2.html", guesshigh=toohigh)
        elif guess < int(qtybreeds):

            toolow = "Your guess is too low, try a higher number!"
            return render_template("datasci2.html", validation=validation, valuecount=valuecount, valuedesc=valuedesc,
                                   fileresult=filenames20, array=labeldata20, arrayresult=arrayresult,
                                   variabledesc=variabledesc,  guesslow=toolow)
        else:
            correctanswer = "Good Guess! 120 is the right answer!!"
            return render_template("datasci2.html", validation=validation, valuecount=valuecount, valuedesc=valuedesc,
                                   fileresult=filenames20, array=labeldata20, arrayresult=arrayresult,
                                   variabledesc=variabledesc, guess=correctanswer)

@app.route('/Modelling')
def Modelling():
    return render_template("datasci3.html")
@app.route('/Modelling', methods=['GET', 'POST'])
def Modellingform():
    if request.form['quizsubmit'] == 'quiz':
        q1 = request.form.get("q1")
        q2 = request.form.get("q2")
        q3 = request.form.get("q3")

        if q1 == "q1correct" and q2 == "q2correct" and q3 == "q3correct":
            quiz_answer = "Great job, you selected the correct answers! Our model needs these components to run analyize our data"
            return render_template("datasci3.html", quiz_answer=quiz_answer)
        elif q1 != "q1correct" or q2 != "q2correct" or q3 != "q3correct":
            quiz_answer = ("One or more of your answers is incorrect, our model compares image tensors to breeds, using Mobilenet_v2")

            return render_template("datasci3.html", quizwronganswer=quiz_answer)





if __name__ == '__main__':
    app.run(debug=True)


