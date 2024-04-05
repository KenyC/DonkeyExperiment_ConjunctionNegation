PennController.ResetPrefix(null)

Sequence( 
    "start",
    "instructions", 
    randomize("trial"),    
    SendResults()
)

// Start screen
newTrial("start",
    newText("sentence0", "We invite you to participate in a research study on language and interpretation.")
        .print()
        .center()
        //.settings.css("font-size", 23 )
        .bold()
    ,
    newCanvas("empty canvas1", 1, 30)
        .print()
    ,
    newText("sentence2", "We will ask you to rate how true a sentence feels to you given a set of objects. The experiment should last about 6 min.")
        .print()
        //.center()
    ,
    newCanvas("empty canvasv", 1, 15)
        .print()
    ,
    newText("Your participation is voluntary and you can decide to quit the experiment at any time.")
        .print()
    ,    
    newText("sentence3", "However, please note that in order to validate the task, you need to complete the experiment and wait until the results are sent (this should take only a few seconds). ")
        .print()
        .bold()
        //.center()
    ,
    newText("Otherwise, we have no way to ensure that you participated at all. ")
        .print()
    ,
    newText("sent5","You will be paid for your participation in this study at the rate posted on Prolific.")
        .print()
        //.center()
    ,
    newCanvas("empty canvasz", 1, 15)
        .print()
    ,
    newText("sentence4", "Your participation in this study will remain confidential. Your individual privacy will be maintained in all published and written data resulting from the study. ")
        .print()
        .center()
    ,
    newCanvas("empty canvas1l", 1, 15)
        .print()
    ,
    newText("sentence5","For further information on the research project, please contact Benjamin Spector <a href=\"mailto:benjamin.spector@ens.psl.eu\">benjamin.spector@ens.psl.eu</a>")
        .print()
        .center()
    ,
    newCanvas("empty canvas2", 1, 30)
        .print()
    ,
    newText("Please enter your Prolific ID.")
        .print()
    ,
    newCanvas("empty canvas111", 1, 15)
        .print()
    ,
    newTextInput("feedback")
        .log()
        .lines(0)
        .size(120, 30)
        .print()
    ,
    newButton("send", "Next")
        .center()
        .print()
        .wait()
)


// Explaining the task
newTrial("instructions",defaultImage.size(100,100),
    newText("sentence0", "Instructions")
        .print()
        .center()
        .bold()
        .settings.css("font-size", 23 )
    ,
    newCanvas("empty canvas0", 1, 15)
        .print()
    ,
    newText("")
        .print()
    ,
    newText("This task includes several trials.")
        .print()
    ,
    newText("In each trial, you will see a picture and a sentence. The picture will contain several geometrical shapes. You will have to rate how true the sentence feels to you as a description of the picture. ")
        .print()
    ,
    newText("There is no \"correct answer\". What we are interested in is your intuitive judgment. ")
        .print()
    ,
    newCanvas("empty canvasq", 1, 15)
        .print()
    ,
    newText("The task is divided into two parts. Each part involves a different type of sentence.")
        .print()
    ,
    newCanvas("empty canvas1", 1, 15)
        .print()
    ,
    newText("Here is an example of a trial:")
        .print()
    ,    
    newCanvas("empty canvas2", 1, 15)
        .print()
    ,
    newText("There is a red square")
        .print()
        .bold()
        .center()
    ,
    newImage("red square", "example.svg")
        .print()
        .center()
    ,
    newScale("scale0", 7)
        .before( newText("left",  "Completely false") )
        .after ( newText("right", "Completely true" ) )
        .center()
        .print()
    ,    
    newCanvas("empty canvas3", 1, 15)
        .print()
    ,
    newText("You should click on the leftmost point.")
        .print()
    ,
    newButton("Start")
        .center()
        .print()
        .wait()
)



Template("trials.csv", row =>
    newTrial("trial", defaultImage.size(250,250),

        newText("sentence", row.sentence)
            .print()
            .center()
            .settings.css("font-size", 23 )
            .bold()
        ,

        newCanvas("empty canvas000", 1, 15)
            .print()
        ,

        newImage("pict", row.filename)
            .print()
            .center()
        ,    
        newCanvas("empty canvas222", 1, 30)
            .print()
        ,
        newScale("score", 7)
            .before(newText("left", "Completely false"))
            .after(newText("right", "Completely true"))
            .center()
            .print()
            .log()
            .wait()
        ,
        newCanvas("empty canvas2", 1, 30)
            .print()
        ,
        newButton("send", "Send")
            .center()
            .print()
            .wait()
    )
    .log("full_condition", row.full_condition)
    .log("trial_no",       row.trial_no)
    // .log("ID" ,            uniqueID)

)