#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.03), April 29, 2015, at 22:18
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Rosvold CPT/N-Back'  # from the Builder filename that created this script
expInfo = {u'Gender': u'female', u'Handedness': u'Right', u'participant': u'SKY100'}

dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if not dlg.OK:
    core.quit()  # user pressed cancel

expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName,
                                 version='',
                                 extraInfo=expInfo,
                                 runtimeInfo=None,
                                 originPath=None,
                                 savePickle=True,
                                 saveWideText=True,
                                 dataFileName=filename
                                 )

# Save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080),
                    fullscr=True,
                    screen=0,
                    allowGUI=False,
                    allowStencil=False,
                    monitor='testMonitor',
                    color=[-1.000,-1.000,-1.000],
                    colorSpace='rgb',
                    blendMode='avg',
                    useFBO=True,
                    )

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Start"
StartClock = core.Clock()
Welcome = visual.TextStim(win=win,
                          ori=0,
                          name='Welcome',
                          text='Welcome to the Biomarker Imaging Study\n\nPress any button when ready to continue',
                          font='Arial',
                          pos=[0, 0],
                          height=0.1,
                          wrapWidth=None,
                          color='white',
                          colorSpace='rgb',
                          opacity=1,
                          depth=0.0
                          )
'''
Total time to record MRI sequence:
    Seconds: 2196.44
    Minutes: 36.60733~
'''
"""
###################SETTINGS######################
###################SETTINGS######################
###################SETTINGS######################
###################SETTINGS######################
"""
#should be 1320 (1320 frames = 22 seconds @ 60Hz refresh rate)
instrStopTime = 12
#should be 1800 (1800 frames = 30 seconds @ 60Hz refresh rate)
instrStopTime2 = 18
#set this to whatever button is recorded on a trigger pulse,
# wrapped in apostrophes and seperated by commas for multiple
# buttons( e.g.: '6','^')
triggerButton = 'num_multiply', '8', '*'
"""
###################SETTINGS######################
###################SETTINGS######################
###################SETTINGS######################
###################SETTINGS######################
"""
"""
#################################################
####################CSV Code#####################
"""


def write_data_file(csv_dictionary, csv_file_name, field_names, final_line={}):
    with open('%s.csv' % csv_file_name, 'wb') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=field_names)
        writer.writeheader()
        row_list = []
        for i in range(len(csv_dictionary[field_names[0]])):
            row_dictionary = {}
            for key in csv_dictionary.keys():
                try:
                    row_dictionary[key] = csv_dictionary[key][i]
                except:
                    pass
            row_list.append(row_dictionary)
        if final_line != {}:
            row_list.append(final_line)
        writer.writerows(row_list)


"""
####################CSV Code#####################
#################################################
"""
"""
#################################################
#################N-Back Code#####################
"""
import csv

iRanWhat = 0
continueRunning = True
while continueRunning:
    corAns = 'none'
    nBackLetter = 'A'
    currentLetter = 'A'
    oldLets = []
    correctButtonList = []
    nBackLets = []
    position = 0
    correctAns = 0
    nBack = 2
    # Array of letters to sample from
    nBackLets = map(chr, range(65, 91))
    counter = 0
    howManyTimes = 10
    while position < howManyTimes:
        # Pick random number from 1-100 for determining if this is an nBack round or not
        bias = randint(1, 100)
        currentLetter = nBackLets[randint(0,25)]
        # Check that enough rounds have passed to display an nBack
        if position-nBack >= 0:
            # Determine if next letter will be new or a nBack match, currently 50/50 odds
            if bias < 50:
                currentLetter = oldLets[position-nBack]
                corAns = '1'
                counter += 1
            else:
                corAns = 'none'
        # update component parameters for each repeat
        correctButtonList.append(corAns)
        oldLets.append(currentLetter)
        position += 1
    iRanWhat += 1
    if counter == (howManyTimes / 2):
        print "nbacks = %d" % counter
        continueRunning = False
        # Load dictionary to write to csvDictionary
        print oldLets
        print correctButtonList
        csvDictionary = {'letters': oldLets, 'correctButton': correctButtonList}
        print csvDictionary

write_data_file(csvDictionary, 'NbackStimOrder', ['letters', 'correctButton'])

print "It took %d runs to get this perfect set." % iRanWhat
"""
##################N-Back Code####################
#################################################
"""
"""
#################################################
####################CPT Code#####################
"""
# RANDOMIZATION OF STIMULI#####
# # Randomization of X trials##
list1 = []
list2 = []
buttonList1 = []
buttonList2 = []
currentLetter = "X"
# Array of letters to sample from
lets = map(chr, range(65, 91))
del lets[23]  # Delete X from the list
xPoolOfLetters = ["X" for i in range(100)]
xPoolOfLetters += (8 * lets)
for i in range(12):
    xPoolOfLetters.append(lets[randint(0,24)])
print len(xPoolOfLetters)

# # Randomization of A-X trials
aCurrentLetter = "A"
print 'length of lets:', len(lets)
aLets = lets
print 'length of alets:', len(aLets)
del aLets[0]
############for ax, I'll just load the list with A's,
############and after sorting insert X after each A in the list
axPoolOfA = ["A" for i in range(100)]
axPoolOfLetters = []
axPoolOfLetters = axPoolOfLetters + (4 * aLets)
for i in range(16):
    axPoolOfLetters.append(aLets[randint(0,23)])
shuffle(axPoolOfLetters)
print len(axPoolOfLetters)

def xRandomizer(pol):
    repeatAttempt = False
    for x in range(0,len(pol)):
        if x > 2:
            if pol[x] == pol[x-1]:
                if pol[x] == pol[x-2]:
                    if pol[x] == pol[x-3]:
                        shuffle(pol)
                        repeatAttempt = True
                        break
    if repeatAttempt == True:
        xRandomizer(pol)
    perfectPool = list(pol)
    print len(perfectPool)
    return perfectPool

def axRandomizer(apoa, apol):
    repeatAttempt = False
    newApol = []
    otherLetters = 0
    aLetters = 0
    totalLength = len(apol)+len(apoa)
    backup1 = list(apoa)
    backup2 = list(apol)
    for x in range(0,totalLength):
        seed = randint(0,2)
        if seed == 0 and apol != []:
            aLetters = 0
            otherLetters += 1
            if x % 2 == 0:
                oLL = 2
            else:
                oLL = 3
            if otherLetters > oLL:
                otherLetters = 0
                if apoa == []:
                    newApol.append(apol.pop())
                else:
                    newApol.append(apoa.pop())
                    aLetters += 1
            else:
                newApol.append(apol.pop())
        elif seed == 1 and apoa != []:
            aLetters += 1
            otherLetters = 0
            if aLetters > 2:
                aLetters = 0
                if apol == []:
                    newApol.append(apoa.pop())
                else:
                    newApol.append(apol.pop())
                    otherLetters += 1
            else:
                newApol.append(apoa.pop())
        else:
            if apol == []:
                if totalLength - len(newApol) > 5:
                    repeatAttempt = True
                    break
                else:
                    newApol.append(apoa.pop())
            elif apoa == []:
                newApol.append(apol.pop())
    if repeatAttempt == True:
        axRandomizer(backup1, backup2)
    else:
        for x in range(0, len(newApol)+100):
            if newApol[x] == 'A':
                newApol.insert(x+1,'X')
    perfectPool = list(newApol)
    print len(perfectPool)
    return perfectPool

list1 = xRandomizer(xPoolOfLetters)
a = list(axPoolOfA)
l = list(axPoolOfLetters)
list2 = axRandomizer(a, l)
#print "list1 = ", list1
#print "list2 = ", list2
def createButtonLists(alist):
    abuttonlist = []
    for i in alist:
        if i is 'X':
            abuttonlist.append('1')
        else:
            abuttonlist.append('none')
    return abuttonlist
buttonList1 = createButtonLists(list1)
buttonList2 = createButtonLists(list2)
#print buttonList1
#print buttonList2
csvDictionary = {'CPT_letters': list1[1:10], 'correctButton':buttonList1[1:10]}
write_data_file(csvDictionary, 'CPTstimOrder1', ['CPT_letters', 'correctButton'])
csvDictionary = {'CPT_letters': list2[1:10], 'correctButton':buttonList2[1:10]}
write_data_file(csvDictionary, 'CPTstimOrder2', ['CPT_letters', 'correctButton'])
####################CPT Code#####################
#################################################

# Initialize components for Routine "AreYouSure"
AreYouSureClock = core.Clock()
Warning = visual.TextStim(win=win, ori=0, name='Warning',
    text="After this point we won't stop the experiment, unless there is a problem.\n\nAre you sure you are ready? If so, press space bar.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "MRI_sync"
MRI_syncClock = core.Clock()
Waiting_For_Pulse = visual.TextStim(win=win, ori=0, name='Waiting_For_Pulse',
    text='Waiting for trigger pulse...',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Welcome_CPT_X"
Welcome_CPT_XClock = core.Clock()
Instructions_CPT_X = visual.TextStim(win=win, ori=0, name='Instructions_CPT_X',
    text='In this task, letters will be presented rapidly on the screen one at a time. Anytime you see the letter X, press button 1 as quickly as you can. Only press when you see letter X.\n\nThis screen will be up for 20 seconds.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "CPT_X"
CPT_XClock = core.Clock()
Letter_CPT_X = visual.TextStim(win=win, ori=0, name='Letter_CPT_X',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
CPT_X_responseList = []
CPT_X_correctList = []
CPT_X_accuracy = []
CPT_X_responseTimeList = []

# Initialize components for Routine "Welcome_CPT_AX"
Welcome_CPT_AXClock = core.Clock()
Instructions_CPT_AX = visual.TextStim(win=win, ori=0, name='Instructions_CPT_AX',
    text='This time press button 1 as quickly as you can when you see the letter X if it comes after letter A. Do not hit the button on letter A, only on letter X when it comes AFTER letter A.\n\nThis screen will be up for 20 seconds.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "CPT_AX"
CPT_AXClock = core.Clock()
Letter_CPT_AX = visual.TextStim(win=win, ori=0, name='Letter_CPT_AX',
    text='default text',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
CPT_AX_responseList = []
CPT_AX_responseToAList = []
CPT_AX_correctList = []
CPT_AX_accuracy = []
CPT_AX_responseTimeList = []

# Initialize components for Routine "Welcome_Nback"
Welcome_NbackClock = core.Clock()
Nback_Instructions = visual.ImageStim(win=win, name='Nback_Instructions',
    image='N-back Instructions.jpg', mask=None,
    ori=0, pos=[0, 0], size=[1.125, 1.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Nback_Fixation"
Nback_FixationClock = core.Clock()
Fixation_Nback = visual.TextStim(win=win, ori=0, name='Fixation_Nback',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Nback_Stimulus"
Nback_StimulusClock = core.Clock()
Letter_Nback = visual.TextStim(win=win, ori=0, name='Letter_Nback',
    text='default text',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
Nback_responseList = []
Nback_correctList = []
Nback_accuracy = []
Nback_responseTimeList = []

# Initialize components for Routine "End"
EndClock = core.Clock()
GoodBye = visual.TextStim(win=win, ori=0, name='GoodBye',
    text='Thank you, the study is complete. Please wait patiently for the technician to assist you out of the MRI.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Start"-------
t = 0
StartClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Next_Slide = event.BuilderKeyResponse()  # create an object of type KeyResponse
Next_Slide.status = NOT_STARTED

# keep track of which components have finished
StartComponents = []
StartComponents.append(Welcome)
StartComponents.append(Next_Slide)
for thisComponent in StartComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Start"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = StartClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome* updates
    if t >= 0.0 and Welcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        Welcome.tStart = t  # underestimates by a little under one frame
        Welcome.frameNStart = frameN  # exact frame index
        Welcome.setAutoDraw(True)
    
    # *Next_Slide* updates
    if t >= 0.0 and Next_Slide.status == NOT_STARTED:
        # keep track of start time/frame for later
        Next_Slide.tStart = t  # underestimates by a little under one frame
        Next_Slide.frameNStart = frameN  # exact frame index
        Next_Slide.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Next_Slide.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Start"-------
for thisComponent in StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


#------Prepare to start Routine "AreYouSure"-------
t = 0
AreYouSureClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Next_Slide_Warning = event.BuilderKeyResponse()  # create an object of type KeyResponse
Next_Slide_Warning.status = NOT_STARTED
# keep track of which components have finished
AreYouSureComponents = []
AreYouSureComponents.append(Warning)
AreYouSureComponents.append(Next_Slide_Warning)
for thisComponent in AreYouSureComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "AreYouSure"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = AreYouSureClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Warning* updates
    if t >= 0.0 and Warning.status == NOT_STARTED:
        # keep track of start time/frame for later
        Warning.tStart = t  # underestimates by a little under one frame
        Warning.frameNStart = frameN  # exact frame index
        Warning.setAutoDraw(True)
    
    # *Next_Slide_Warning* updates
    if t >= 0.0 and Next_Slide_Warning.status == NOT_STARTED:
        # keep track of start time/frame for later
        Next_Slide_Warning.tStart = t  # underestimates by a little under one frame
        Next_Slide_Warning.frameNStart = frameN  # exact frame index
        Next_Slide_Warning.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Next_Slide_Warning.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AreYouSureComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "AreYouSure"-------
for thisComponent in AreYouSureComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "MRI_sync"-------
t = 0
MRI_syncClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Pulse_Next_Slide = event.BuilderKeyResponse()  # create an object of type KeyResponse
Pulse_Next_Slide.status = NOT_STARTED
# keep track of which components have finished
MRI_syncComponents = []
MRI_syncComponents.append(Waiting_For_Pulse)
MRI_syncComponents.append(Pulse_Next_Slide)
for thisComponent in MRI_syncComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "MRI_sync"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = MRI_syncClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Waiting_For_Pulse* updates
    if t >= 0.0 and Waiting_For_Pulse.status == NOT_STARTED:
        # keep track of start time/frame for later
        Waiting_For_Pulse.tStart = t  # underestimates by a little under one frame
        Waiting_For_Pulse.frameNStart = frameN  # exact frame index
        Waiting_For_Pulse.setAutoDraw(True)
    
    # *Pulse_Next_Slide* updates
    if t >= 0.0 and Pulse_Next_Slide.status == NOT_STARTED:
        # keep track of start time/frame for later
        Pulse_Next_Slide.tStart = t  # underestimates by a little under one frame
        Pulse_Next_Slide.frameNStart = frameN  # exact frame index
        Pulse_Next_Slide.status = STARTED
        # AllowedKeys looks like a variable named `triggerButton`
        if not 'triggerButton' in locals():
            logging.error('AllowedKeys variable `triggerButton` is not defined.')
            core.quit()
        if not type(triggerButton) in [list, tuple, np.ndarray]:
            if not isinstance(triggerButton, basestring):
                logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                core.quit()
            elif not ',' in triggerButton: triggerButton = (triggerButton,)
            else:  triggerButton = eval(triggerButton)
        # keyboard checking is just starting
        Pulse_Next_Slide.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if Pulse_Next_Slide.status == STARTED:
        theseKeys = event.getKeys(keyList=list(triggerButton))
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Pulse_Next_Slide.keys.extend(theseKeys)  # storing all keys
            Pulse_Next_Slide.rt.append(Pulse_Next_Slide.clock.getTime())
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MRI_syncComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "MRI_sync"-------
for thisComponent in MRI_syncComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Pulse_Next_Slide.keys in ['', [], None]:  # No response was made
   Pulse_Next_Slide.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Pulse_Next_Slide.keys',Pulse_Next_Slide.keys)
if Pulse_Next_Slide.keys != None:  # we had a response
    thisExp.addData('Pulse_Next_Slide.rt', Pulse_Next_Slide.rt)
thisExp.nextEntry()

#------Prepare to start Routine "Welcome_CPT_X"-------
t = 0
Welcome_CPT_XClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Trigger_CPT_X_Instructions = event.BuilderKeyResponse()  # create an object of type KeyResponse
Trigger_CPT_X_Instructions.status = NOT_STARTED
# keep track of which components have finished
Welcome_CPT_XComponents = []
Welcome_CPT_XComponents.append(Instructions_CPT_X)
Welcome_CPT_XComponents.append(Trigger_CPT_X_Instructions)
for thisComponent in Welcome_CPT_XComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Welcome_CPT_X"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Welcome_CPT_XClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions_CPT_X* updates
    if frameN >= 0 and Instructions_CPT_X.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions_CPT_X.tStart = t  # underestimates by a little under one frame
        Instructions_CPT_X.frameNStart = frameN  # exact frame index
        Instructions_CPT_X.setAutoDraw(True)
    if Instructions_CPT_X.status == STARTED and frameN >= instrStopTime-120:
        Instructions_CPT_X.setAutoDraw(False)
    
    # *Trigger_CPT_X_Instructions* updates
    if frameN >= 0.0 and Trigger_CPT_X_Instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        Trigger_CPT_X_Instructions.tStart = t  # underestimates by a little under one frame
        Trigger_CPT_X_Instructions.frameNStart = frameN  # exact frame index
        Trigger_CPT_X_Instructions.status = STARTED
        # AllowedKeys looks like a variable named `triggerButton`
        if not 'triggerButton' in locals():
            logging.error('AllowedKeys variable `triggerButton` is not defined.')
            core.quit()
        if not type(triggerButton) in [list, tuple, np.ndarray]:
            if not isinstance(triggerButton, basestring):
                logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                core.quit()
            elif not ',' in triggerButton: triggerButton = (triggerButton,)
            else:  triggerButton = eval(triggerButton)
        # keyboard checking is just starting
        Trigger_CPT_X_Instructions.clock.reset()  # now t=0
    if Trigger_CPT_X_Instructions.status == STARTED and frameN >= instrStopTime:
        Trigger_CPT_X_Instructions.status = STOPPED
    if Trigger_CPT_X_Instructions.status == STARTED:
        theseKeys = event.getKeys(keyList=list(triggerButton))
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Trigger_CPT_X_Instructions.keys.extend(theseKeys)  # storing all keys
            Trigger_CPT_X_Instructions.rt.append(Trigger_CPT_X_Instructions.clock.getTime())
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_CPT_XComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Welcome_CPT_X"-------
for thisComponent in Welcome_CPT_XComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Trigger_CPT_X_Instructions.keys in ['', [], None]:  # No response was made
   Trigger_CPT_X_Instructions.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Trigger_CPT_X_Instructions.keys',Trigger_CPT_X_Instructions.keys)
if Trigger_CPT_X_Instructions.keys != None:  # we had a response
    thisExp.addData('Trigger_CPT_X_Instructions.rt', Trigger_CPT_X_Instructions.rt)
thisExp.nextEntry()

# set up handler to look after randomisation of conditions etc
CPT_X_Trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('CPTstimOrder1.csv'),
    seed=None, name='CPT_X_Trials')
thisExp.addLoop(CPT_X_Trials)  # add the loop to the experiment
thisCPT_X_Trial = CPT_X_Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisCPT_X_Trial.rgb)
if thisCPT_X_Trial != None:
    for paramName in thisCPT_X_Trial.keys():
        exec(paramName + '= thisCPT_X_Trial.' + paramName)

for thisCPT_X_Trial in CPT_X_Trials:
    currentLoop = CPT_X_Trials
    # abbreviate parameter names if possible (e.g. rgb = thisCPT_X_Trial.rgb)
    if thisCPT_X_Trial != None:
        for paramName in thisCPT_X_Trial.keys():
            exec(paramName + '= thisCPT_X_Trial.' + paramName)
    
    #------Prepare to start Routine "CPT_X"-------
    t = 0
    CPT_XClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    Letter_CPT_X.setText(CPT_letters)
    Response_CPT_X_X = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Response_CPT_X_X.status = NOT_STARTED
    Trigger_CPT_X_Stimulus = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Trigger_CPT_X_Stimulus.status = NOT_STARTED
    
    # keep track of which components have finished
    CPT_XComponents = []
    CPT_XComponents.append(Letter_CPT_X)
    CPT_XComponents.append(Response_CPT_X_X)
    CPT_XComponents.append(Trigger_CPT_X_Stimulus)
    for thisComponent in CPT_XComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "CPT_X"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CPT_XClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Letter_CPT_X* updates
        if frameN >= 0 and Letter_CPT_X.status == NOT_STARTED:
            # keep track of start time/frame for later
            Letter_CPT_X.tStart = t  # underestimates by a little under one frame
            Letter_CPT_X.frameNStart = frameN  # exact frame index
            Letter_CPT_X.setAutoDraw(True)
        if Letter_CPT_X.status == STARTED and frameN >= 6:
            Letter_CPT_X.setAutoDraw(False)
        
        # *Response_CPT_X_X* updates
        if frameN >= 0 and Response_CPT_X_X.status == NOT_STARTED:
            # keep track of start time/frame for later
            Response_CPT_X_X.tStart = t  # underestimates by a little under one frame
            Response_CPT_X_X.frameNStart = frameN  # exact frame index
            Response_CPT_X_X.status = STARTED
            # keyboard checking is just starting
            Response_CPT_X_X.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Response_CPT_X_X.status == STARTED and frameN >= 60:
            Response_CPT_X_X.status = STOPPED
        if Response_CPT_X_X.status == STARTED:
            theseKeys = event.getKeys(keyList=['1'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Response_CPT_X_X.keys = theseKeys[-1]  # just the last key pressed
                Response_CPT_X_X.rt = Response_CPT_X_X.clock.getTime()
                # was this 'correct'?
                if (Response_CPT_X_X.keys == str(correctButton)) or (Response_CPT_X_X.keys == correctButton):
                    Response_CPT_X_X.corr = 1
                else:
                    Response_CPT_X_X.corr = 0
        
        # *Trigger_CPT_X_Stimulus* updates
        if frameN >= 0 and Trigger_CPT_X_Stimulus.status == NOT_STARTED:
            # keep track of start time/frame for later
            Trigger_CPT_X_Stimulus.tStart = t  # underestimates by a little under one frame
            Trigger_CPT_X_Stimulus.frameNStart = frameN  # exact frame index
            Trigger_CPT_X_Stimulus.status = STARTED
            # AllowedKeys looks like a variable named `triggerButton`
            if not 'triggerButton' in locals():
                logging.error('AllowedKeys variable `triggerButton` is not defined.')
                core.quit()
            if not type(triggerButton) in [list, tuple, np.ndarray]:
                if not isinstance(triggerButton, basestring):
                    logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                    core.quit()
                elif not ',' in triggerButton: triggerButton = (triggerButton,)
                else:  triggerButton = eval(triggerButton)
            # keyboard checking is just starting
            Trigger_CPT_X_Stimulus.clock.reset()  # now t=0
        if Trigger_CPT_X_Stimulus.status == STARTED and frameN >= 60:
            Trigger_CPT_X_Stimulus.status = STOPPED
        if Trigger_CPT_X_Stimulus.status == STARTED:
            theseKeys = event.getKeys(keyList=list(triggerButton))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Trigger_CPT_X_Stimulus.keys.extend(theseKeys)  # storing all keys
                Trigger_CPT_X_Stimulus.rt.append(Trigger_CPT_X_Stimulus.clock.getTime())
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CPT_XComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "CPT_X"-------
    for thisComponent in CPT_XComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Response_CPT_X_X.keys in ['', [], None]:  # No response was made
       Response_CPT_X_X.keys=None
       # was no response the correct answer?!
       if str(correctButton).lower() == 'none': Response_CPT_X_X.corr = 1  # correct non-response
       else: Response_CPT_X_X.corr = 0  # failed to respond (incorrectly)
    # store data for CPT_X_Trials (TrialHandler)
    CPT_X_Trials.addData('Response_CPT_X_X.keys',Response_CPT_X_X.keys)
    CPT_X_Trials.addData('Response_CPT_X_X.corr', Response_CPT_X_X.corr)
    if Response_CPT_X_X.keys != None:  # we had a response
        CPT_X_Trials.addData('Response_CPT_X_X.rt', Response_CPT_X_X.rt)
    # check responses
    if Trigger_CPT_X_Stimulus.keys in ['', [], None]:  # No response was made
       Trigger_CPT_X_Stimulus.keys=None
    # store data for CPT_X_Trials (TrialHandler)
    CPT_X_Trials.addData('Trigger_CPT_X_Stimulus.keys',Trigger_CPT_X_Stimulus.keys)
    if Trigger_CPT_X_Stimulus.keys != None:  # we had a response
        CPT_X_Trials.addData('Trigger_CPT_X_Stimulus.rt', Trigger_CPT_X_Stimulus.rt)
    print 'Response_CPT_X_X.keys = %s' % Response_CPT_X_X.keys
    CPT_X_responseList.append(Response_CPT_X_X.keys)
    print 'CPT_X_responseList = %s' % CPT_X_responseList
    CPT_X_correctList.append(Response_CPT_X_X.corr)
    if len(CPT_X_accuracy) > 0:
        CPT_X_accuracy.append(sum(CPT_X_correctList)/len(CPT_X_correctList))
    else:
        CPT_X_accuracy.append(Response_CPT_X_X.corr)
    if Response_CPT_X_X.keys != None:  # we had a response
        CPT_X_responseTimeList.append(Response_CPT_X_X.rt)
    else:
        CPT_X_responseTimeList.append(0)
    thisExp.nextEntry()
    
# completed 1 repeats of 'CPT_X_Trials'

# get names of stimulus parameters
if CPT_X_Trials.trialList in ([], [None], None):  params = []
else:  params = CPT_X_Trials.trialList[0].keys()
# save data for this loop
CPT_X_Trials.saveAsExcel(filename + '.xlsx', sheetName='CPT_X_Trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
CPT_X_Trials.saveAsText(filename + 'CPT_X_Trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "Welcome_CPT_AX"-------
t = 0
Welcome_CPT_AXClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Trigger_CPT_AX_Instructions = event.BuilderKeyResponse()  # create an object of type KeyResponse
Trigger_CPT_AX_Instructions.status = NOT_STARTED
# keep track of which components have finished
Welcome_CPT_AXComponents = []
Welcome_CPT_AXComponents.append(Instructions_CPT_AX)
Welcome_CPT_AXComponents.append(Trigger_CPT_AX_Instructions)
for thisComponent in Welcome_CPT_AXComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Welcome_CPT_AX"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Welcome_CPT_AXClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions_CPT_AX* updates
    if frameN >= 0 and Instructions_CPT_AX.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions_CPT_AX.tStart = t  # underestimates by a little under one frame
        Instructions_CPT_AX.frameNStart = frameN  # exact frame index
        Instructions_CPT_AX.setAutoDraw(True)
    if Instructions_CPT_AX.status == STARTED and frameN >= instrStopTime-120:
        Instructions_CPT_AX.setAutoDraw(False)
    
    # *Trigger_CPT_AX_Instructions* updates
    if frameN >= 0 and Trigger_CPT_AX_Instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        Trigger_CPT_AX_Instructions.tStart = t  # underestimates by a little under one frame
        Trigger_CPT_AX_Instructions.frameNStart = frameN  # exact frame index
        Trigger_CPT_AX_Instructions.status = STARTED
        # AllowedKeys looks like a variable named `triggerButton`
        if not 'triggerButton' in locals():
            logging.error('AllowedKeys variable `triggerButton` is not defined.')
            core.quit()
        if not type(triggerButton) in [list, tuple, np.ndarray]:
            if not isinstance(triggerButton, basestring):
                logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                core.quit()
            elif not ',' in triggerButton: triggerButton = (triggerButton,)
            else:  triggerButton = eval(triggerButton)
        # keyboard checking is just starting
        Trigger_CPT_AX_Instructions.clock.reset()  # now t=0
    if Trigger_CPT_AX_Instructions.status == STARTED and frameN >= instrStopTime:
        Trigger_CPT_AX_Instructions.status = STOPPED
    if Trigger_CPT_AX_Instructions.status == STARTED:
        theseKeys = event.getKeys(keyList=list(triggerButton))
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Trigger_CPT_AX_Instructions.keys.extend(theseKeys)  # storing all keys
            Trigger_CPT_AX_Instructions.rt.append(Trigger_CPT_AX_Instructions.clock.getTime())
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_CPT_AXComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Welcome_CPT_AX"-------
for thisComponent in Welcome_CPT_AXComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Trigger_CPT_AX_Instructions.keys in ['', [], None]:  # No response was made
   Trigger_CPT_AX_Instructions.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Trigger_CPT_AX_Instructions.keys',Trigger_CPT_AX_Instructions.keys)
if Trigger_CPT_AX_Instructions.keys != None:  # we had a response
    thisExp.addData('Trigger_CPT_AX_Instructions.rt', Trigger_CPT_AX_Instructions.rt)
thisExp.nextEntry()

# set up handler to look after randomisation of conditions etc
CPT_AX_Trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('CPTstimOrder2.csv'),
    seed=None, name='CPT_AX_Trials')
thisExp.addLoop(CPT_AX_Trials)  # add the loop to the experiment
thisCPT_AX_Trial = CPT_AX_Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisCPT_AX_Trial.rgb)
if thisCPT_AX_Trial != None:
    for paramName in thisCPT_AX_Trial.keys():
        exec(paramName + '= thisCPT_AX_Trial.' + paramName)

for thisCPT_AX_Trial in CPT_AX_Trials:
    currentLoop = CPT_AX_Trials
    # abbreviate parameter names if possible (e.g. rgb = thisCPT_AX_Trial.rgb)
    if thisCPT_AX_Trial != None:
        for paramName in thisCPT_AX_Trial.keys():
            exec(paramName + '= thisCPT_AX_Trial.' + paramName)
    
    #------Prepare to start Routine "CPT_AX"-------
    t = 0
    CPT_AXClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    Letter_CPT_AX.setText(CPT_letters)
    Response_CPT_AX_X = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Response_CPT_AX_X.status = NOT_STARTED
    Response_CPT_AX_A = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Response_CPT_AX_A.status = NOT_STARTED
    Trigger_CPT_AX_Stimuls = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Trigger_CPT_AX_Stimuls.status = NOT_STARTED
    
    # keep track of which components have finished
    CPT_AXComponents = []
    CPT_AXComponents.append(Letter_CPT_AX)
    CPT_AXComponents.append(Response_CPT_AX_X)
    CPT_AXComponents.append(Response_CPT_AX_A)
    CPT_AXComponents.append(Trigger_CPT_AX_Stimuls)
    for thisComponent in CPT_AXComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "CPT_AX"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CPT_AXClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Letter_CPT_AX* updates
        if frameN >= 0 and Letter_CPT_AX.status == NOT_STARTED:
            # keep track of start time/frame for later
            Letter_CPT_AX.tStart = t  # underestimates by a little under one frame
            Letter_CPT_AX.frameNStart = frameN  # exact frame index
            Letter_CPT_AX.setAutoDraw(True)
        if Letter_CPT_AX.status == STARTED and frameN >= 6:
            Letter_CPT_AX.setAutoDraw(False)
        
        # *Response_CPT_AX_X* updates
        if frameN >= 0 and Response_CPT_AX_X.status == NOT_STARTED:
            # keep track of start time/frame for later
            Response_CPT_AX_X.tStart = t  # underestimates by a little under one frame
            Response_CPT_AX_X.frameNStart = frameN  # exact frame index
            Response_CPT_AX_X.status = STARTED
            # keyboard checking is just starting
            Response_CPT_AX_X.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Response_CPT_AX_X.status == STARTED and frameN >= 60:
            Response_CPT_AX_X.status = STOPPED
        if Response_CPT_AX_X.status == STARTED:
            theseKeys = event.getKeys(keyList=['1'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Response_CPT_AX_X.keys = theseKeys[-1]  # just the last key pressed
                Response_CPT_AX_X.rt = Response_CPT_AX_X.clock.getTime()
                # was this 'correct'?
                if (Response_CPT_AX_X.keys == str(correctButton)) or (Response_CPT_AX_X.keys == correctButton):
                    Response_CPT_AX_X.corr = 1
                else:
                    Response_CPT_AX_X.corr = 0
        
        # *Response_CPT_AX_A* updates
        if frameN >= 0 and Response_CPT_AX_A.status == NOT_STARTED:
            # keep track of start time/frame for later
            Response_CPT_AX_A.tStart = t  # underestimates by a little under one frame
            Response_CPT_AX_A.frameNStart = frameN  # exact frame index
            Response_CPT_AX_A.status = STARTED
            # keyboard checking is just starting
            Response_CPT_AX_A.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Response_CPT_AX_A.status == STARTED and frameN >= 60:
            Response_CPT_AX_A.status = STOPPED
        if Response_CPT_AX_A.status == STARTED:
            theseKeys = event.getKeys(keyList=['1'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Response_CPT_AX_A.keys = theseKeys[-1]  # just the last key pressed
                Response_CPT_AX_A.rt = Response_CPT_AX_A.clock.getTime()
        
        # *Trigger_CPT_AX_Stimuls* updates
        if frameN >= 0 and Trigger_CPT_AX_Stimuls.status == NOT_STARTED:
            # keep track of start time/frame for later
            Trigger_CPT_AX_Stimuls.tStart = t  # underestimates by a little under one frame
            Trigger_CPT_AX_Stimuls.frameNStart = frameN  # exact frame index
            Trigger_CPT_AX_Stimuls.status = STARTED
            # AllowedKeys looks like a variable named `triggerButton`
            if not 'triggerButton' in locals():
                logging.error('AllowedKeys variable `triggerButton` is not defined.')
                core.quit()
            if not type(triggerButton) in [list, tuple, np.ndarray]:
                if not isinstance(triggerButton, basestring):
                    logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                    core.quit()
                elif not ',' in triggerButton: triggerButton = (triggerButton,)
                else:  triggerButton = eval(triggerButton)
            # keyboard checking is just starting
            Trigger_CPT_AX_Stimuls.clock.reset()  # now t=0
        if Trigger_CPT_AX_Stimuls.status == STARTED and frameN >= 60:
            Trigger_CPT_AX_Stimuls.status = STOPPED
        if Trigger_CPT_AX_Stimuls.status == STARTED:
            theseKeys = event.getKeys(keyList=list(triggerButton))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Trigger_CPT_AX_Stimuls.keys.extend(theseKeys)  # storing all keys
                Trigger_CPT_AX_Stimuls.rt.append(Trigger_CPT_AX_Stimuls.clock.getTime())
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CPT_AXComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "CPT_AX"-------
    for thisComponent in CPT_AXComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Response_CPT_AX_X.keys in ['', [], None]:  # No response was made
       Response_CPT_AX_X.keys=None
       # was no response the correct answer?!
       if str(correctButton).lower() == 'none': Response_CPT_AX_X.corr = 1  # correct non-response
       else: Response_CPT_AX_X.corr = 0  # failed to respond (incorrectly)
    # store data for CPT_AX_Trials (TrialHandler)
    CPT_AX_Trials.addData('Response_CPT_AX_X.keys',Response_CPT_AX_X.keys)
    CPT_AX_Trials.addData('Response_CPT_AX_X.corr', Response_CPT_AX_X.corr)
    if Response_CPT_AX_X.keys != None:  # we had a response
        CPT_AX_Trials.addData('Response_CPT_AX_X.rt', Response_CPT_AX_X.rt)
    # check responses
    if Response_CPT_AX_A.keys in ['', [], None]:  # No response was made
       Response_CPT_AX_A.keys=None
    # store data for CPT_AX_Trials (TrialHandler)
    CPT_AX_Trials.addData('Response_CPT_AX_A.keys',Response_CPT_AX_A.keys)
    if Response_CPT_AX_A.keys != None:  # we had a response
        CPT_AX_Trials.addData('Response_CPT_AX_A.rt', Response_CPT_AX_A.rt)
    # check responses
    if Trigger_CPT_AX_Stimuls.keys in ['', [], None]:  # No response was made
       Trigger_CPT_AX_Stimuls.keys=None
    # store data for CPT_AX_Trials (TrialHandler)
    CPT_AX_Trials.addData('Trigger_CPT_AX_Stimuls.keys',Trigger_CPT_AX_Stimuls.keys)
    if Trigger_CPT_AX_Stimuls.keys != None:  # we had a response
        CPT_AX_Trials.addData('Trigger_CPT_AX_Stimuls.rt', Trigger_CPT_AX_Stimuls.rt)
    CPT_AX_responseList.append(Response_CPT_AX_X.keys)
    CPT_AX_correctList.append(Response_CPT_AX_X.corr)
    if (Response_CPT_AX_X.corr == 0) and (CPT_letters == 'A'):
        CPT_AX_responseToAList.append(1)
    else:
        CPT_AX_responseToAList.append(0)
    if len(CPT_AX_accuracy) > 0:
        CPT_AX_accuracy.append(sum(CPT_AX_correctList)/len(CPT_AX_correctList))
    else:
        CPT_AX_accuracy.append(Response_CPT_AX_X.corr)
    if Response_CPT_AX_X.keys != None:  # we had a response
        CPT_AX_responseTimeList.append(Response_CPT_AX_X.rt)
    else:
        CPT_AX_responseTimeList.append(0)
    thisExp.nextEntry()
    
# completed 1 repeats of 'CPT_AX_Trials'

# get names of stimulus parameters
if CPT_AX_Trials.trialList in ([], [None], None):  params = []
else:  params = CPT_AX_Trials.trialList[0].keys()
# save data for this loop
CPT_AX_Trials.saveAsExcel(filename + '.xlsx', sheetName='CPT_AX_Trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
CPT_AX_Trials.saveAsText(filename + 'CPT_AX_Trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "Welcome_Nback"-------
t = 0
Welcome_NbackClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Trigger_Nback_Instructions = event.BuilderKeyResponse()  # create an object of type KeyResponse
Trigger_Nback_Instructions.status = NOT_STARTED
# keep track of which components have finished
Welcome_NbackComponents = []
Welcome_NbackComponents.append(Nback_Instructions)
Welcome_NbackComponents.append(Trigger_Nback_Instructions)
for thisComponent in Welcome_NbackComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Welcome_Nback"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Welcome_NbackClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Nback_Instructions* updates
    if frameN >= 0 and Nback_Instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        Nback_Instructions.tStart = t  # underestimates by a little under one frame
        Nback_Instructions.frameNStart = frameN  # exact frame index
        Nback_Instructions.setAutoDraw(True)
    if Nback_Instructions.status == STARTED and frameN >= instrStopTime2:
        Nback_Instructions.setAutoDraw(False)
    
    # *Trigger_Nback_Instructions* updates
    if frameN >= 0 and Trigger_Nback_Instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        Trigger_Nback_Instructions.tStart = t  # underestimates by a little under one frame
        Trigger_Nback_Instructions.frameNStart = frameN  # exact frame index
        Trigger_Nback_Instructions.status = STARTED
        # AllowedKeys looks like a variable named `triggerButton`
        if not 'triggerButton' in locals():
            logging.error('AllowedKeys variable `triggerButton` is not defined.')
            core.quit()
        if not type(triggerButton) in [list, tuple, np.ndarray]:
            if not isinstance(triggerButton, basestring):
                logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                core.quit()
            elif not ',' in triggerButton: triggerButton = (triggerButton,)
            else:  triggerButton = eval(triggerButton)
        # keyboard checking is just starting
        Trigger_Nback_Instructions.clock.reset()  # now t=0
    if Trigger_Nback_Instructions.status == STARTED and frameN >= instrStopTime2:
        Trigger_Nback_Instructions.status = STOPPED
    if Trigger_Nback_Instructions.status == STARTED:
        theseKeys = event.getKeys(keyList=list(triggerButton))
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Trigger_Nback_Instructions.keys.extend(theseKeys)  # storing all keys
            Trigger_Nback_Instructions.rt.append(Trigger_Nback_Instructions.clock.getTime())
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_NbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Welcome_Nback"-------
for thisComponent in Welcome_NbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Trigger_Nback_Instructions.keys in ['', [], None]:  # No response was made
   Trigger_Nback_Instructions.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Trigger_Nback_Instructions.keys',Trigger_Nback_Instructions.keys)
if Trigger_Nback_Instructions.keys != None:  # we had a response
    thisExp.addData('Trigger_Nback_Instructions.rt', Trigger_Nback_Instructions.rt)
thisExp.nextEntry()

# set up handler to look after randomisation of conditions etc
Nback_Trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('NbackStimOrder.csv'),
    seed=None, name='Nback_Trials')
thisExp.addLoop(Nback_Trials)  # add the loop to the experiment
thisNback_Trial = Nback_Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisNback_Trial.rgb)
if thisNback_Trial != None:
    for paramName in thisNback_Trial.keys():
        exec(paramName + '= thisNback_Trial.' + paramName)

for thisNback_Trial in Nback_Trials:
    currentLoop = Nback_Trials
    # abbreviate parameter names if possible (e.g. rgb = thisNback_Trial.rgb)
    if thisNback_Trial != None:
        for paramName in thisNback_Trial.keys():
            exec(paramName + '= thisNback_Trial.' + paramName)
    
    #------Prepare to start Routine "Nback_Fixation"-------
    t = 0
    Nback_FixationClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    Trigger_Nback_Fixation = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Trigger_Nback_Fixation.status = NOT_STARTED
    # keep track of which components have finished
    Nback_FixationComponents = []
    Nback_FixationComponents.append(Fixation_Nback)
    Nback_FixationComponents.append(Trigger_Nback_Fixation)
    for thisComponent in Nback_FixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Nback_Fixation"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Nback_FixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_Nback* updates
        if frameN >= 0 and Fixation_Nback.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation_Nback.tStart = t  # underestimates by a little under one frame
            Fixation_Nback.frameNStart = frameN  # exact frame index
            Fixation_Nback.setAutoDraw(True)
        if Fixation_Nback.status == STARTED and frameN >= 60:
            Fixation_Nback.setAutoDraw(False)
        
        # *Trigger_Nback_Fixation* updates
        if frameN >= 0 and Trigger_Nback_Fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            Trigger_Nback_Fixation.tStart = t  # underestimates by a little under one frame
            Trigger_Nback_Fixation.frameNStart = frameN  # exact frame index
            Trigger_Nback_Fixation.status = STARTED
            # AllowedKeys looks like a variable named `triggerButton`
            if not 'triggerButton' in locals():
                logging.error('AllowedKeys variable `triggerButton` is not defined.')
                core.quit()
            if not type(triggerButton) in [list, tuple, np.ndarray]:
                if not isinstance(triggerButton, basestring):
                    logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                    core.quit()
                elif not ',' in triggerButton: triggerButton = (triggerButton,)
                else:  triggerButton = eval(triggerButton)
            # keyboard checking is just starting
            Trigger_Nback_Fixation.clock.reset()  # now t=0
        if Trigger_Nback_Fixation.status == STARTED and frameN >= 60:
            Trigger_Nback_Fixation.status = STOPPED
        if Trigger_Nback_Fixation.status == STARTED:
            theseKeys = event.getKeys(keyList=list(triggerButton))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Trigger_Nback_Fixation.keys.extend(theseKeys)  # storing all keys
                Trigger_Nback_Fixation.rt.append(Trigger_Nback_Fixation.clock.getTime())
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Nback_FixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Nback_Fixation"-------
    for thisComponent in Nback_FixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Trigger_Nback_Fixation.keys in ['', [], None]:  # No response was made
       Trigger_Nback_Fixation.keys=None
    # store data for Nback_Trials (TrialHandler)
    Nback_Trials.addData('Trigger_Nback_Fixation.keys',Trigger_Nback_Fixation.keys)
    if Trigger_Nback_Fixation.keys != None:  # we had a response
        Nback_Trials.addData('Trigger_Nback_Fixation.rt', Trigger_Nback_Fixation.rt)
    
    #------Prepare to start Routine "Nback_Stimulus"-------
    t = 0
    Nback_StimulusClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    Letter_Nback.setText(letters)
    Response_Nback = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Response_Nback.status = NOT_STARTED
    Trigger_Nback_Stimulus = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Trigger_Nback_Stimulus.status = NOT_STARTED
    
    # keep track of which components have finished
    Nback_StimulusComponents = []
    Nback_StimulusComponents.append(Letter_Nback)
    Nback_StimulusComponents.append(Response_Nback)
    Nback_StimulusComponents.append(Trigger_Nback_Stimulus)
    for thisComponent in Nback_StimulusComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Nback_Stimulus"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Nback_StimulusClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Letter_Nback* updates
        if frameN >= 0 and Letter_Nback.status == NOT_STARTED:
            # keep track of start time/frame for later
            Letter_Nback.tStart = t  # underestimates by a little under one frame
            Letter_Nback.frameNStart = frameN  # exact frame index
            Letter_Nback.setAutoDraw(True)
        if Letter_Nback.status == STARTED and frameN >= 60:
            Letter_Nback.setAutoDraw(False)
        
        # *Response_Nback* updates
        if frameN >= 0 and Response_Nback.status == NOT_STARTED:
            # keep track of start time/frame for later
            Response_Nback.tStart = t  # underestimates by a little under one frame
            Response_Nback.frameNStart = frameN  # exact frame index
            Response_Nback.status = STARTED
            # keyboard checking is just starting
            Response_Nback.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Response_Nback.status == STARTED and frameN >= 60:
            Response_Nback.status = STOPPED
        if Response_Nback.status == STARTED:
            theseKeys = event.getKeys(keyList=['1'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Response_Nback.keys = theseKeys[-1]  # just the last key pressed
                Response_Nback.rt = Response_Nback.clock.getTime()
                # was this 'correct'?
                if (Response_Nback.keys == str(correctButton)) or (Response_Nback.keys == correctButton):
                    Response_Nback.corr = 1
                else:
                    Response_Nback.corr = 0
        
        # *Trigger_Nback_Stimulus* updates
        if frameN >= 0 and Trigger_Nback_Stimulus.status == NOT_STARTED:
            # keep track of start time/frame for later
            Trigger_Nback_Stimulus.tStart = t  # underestimates by a little under one frame
            Trigger_Nback_Stimulus.frameNStart = frameN  # exact frame index
            Trigger_Nback_Stimulus.status = STARTED
            # AllowedKeys looks like a variable named `triggerButton`
            if not 'triggerButton' in locals():
                logging.error('AllowedKeys variable `triggerButton` is not defined.')
                core.quit()
            if not type(triggerButton) in [list, tuple, np.ndarray]:
                if not isinstance(triggerButton, basestring):
                    logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                    core.quit()
                elif not ',' in triggerButton: triggerButton = (triggerButton,)
                else:  triggerButton = eval(triggerButton)
            # keyboard checking is just starting
            Trigger_Nback_Stimulus.clock.reset()  # now t=0
        if Trigger_Nback_Stimulus.status == STARTED and frameN >= 60:
            Trigger_Nback_Stimulus.status = STOPPED
        if Trigger_Nback_Stimulus.status == STARTED:
            theseKeys = event.getKeys(keyList=list(triggerButton))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Trigger_Nback_Stimulus.keys.extend(theseKeys)  # storing all keys
                Trigger_Nback_Stimulus.rt.append(Trigger_Nback_Stimulus.clock.getTime())
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Nback_StimulusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Nback_Stimulus"-------
    for thisComponent in Nback_StimulusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Response_Nback.keys in ['', [], None]:  # No response was made
       Response_Nback.keys=None
       # was no response the correct answer?!
       if str(correctButton).lower() == 'none': Response_Nback.corr = 1  # correct non-response
       else: Response_Nback.corr = 0  # failed to respond (incorrectly)
    # store data for Nback_Trials (TrialHandler)
    Nback_Trials.addData('Response_Nback.keys',Response_Nback.keys)
    Nback_Trials.addData('Response_Nback.corr', Response_Nback.corr)
    if Response_Nback.keys != None:  # we had a response
        Nback_Trials.addData('Response_Nback.rt', Response_Nback.rt)
    # check responses
    if Trigger_Nback_Stimulus.keys in ['', [], None]:  # No response was made
       Trigger_Nback_Stimulus.keys=None
    # store data for Nback_Trials (TrialHandler)
    Nback_Trials.addData('Trigger_Nback_Stimulus.keys',Trigger_Nback_Stimulus.keys)
    if Trigger_Nback_Stimulus.keys != None:  # we had a response
        Nback_Trials.addData('Trigger_Nback_Stimulus.rt', Trigger_Nback_Stimulus.rt)
    Nback_responseList.append(Response_Nback.keys)
    print 'Response_Nback.keys = %s' % Response_Nback.keys
    print 'Nback_responseList = %s' % Nback_responseList
    Nback_correctList.append(Response_Nback.corr)
    if len(Nback_accuracy) > 0:
        Nback_accuracy.append(sum(Nback_correctList)/len(Nback_correctList))
    else:
        Nback_accuracy.append(Response_Nback.corr)
    if Response_Nback.keys != None:  # we had a response
        Nback_responseTimeList.append(Response_Nback.rt)
    else:
        Nback_responseTimeList.append(0)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Nback_Trials'

# get names of stimulus parameters
if Nback_Trials.trialList in ([], [None], None):  params = []
else:  params = Nback_Trials.trialList[0].keys()
# save data for this loop
Nback_Trials.saveAsExcel(filename + '.xlsx', sheetName='Nback_Trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
Nback_Trials.saveAsText(filename + 'Nback_Trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = []
EndComponents.append(GoodBye)
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "End"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GoodBye* updates
    if frameN >= 0.0 and GoodBye.status == NOT_STARTED:
        # keep track of start time/frame for later
        GoodBye.tStart = t  # underestimates by a little under one frame
        GoodBye.frameNStart = frameN  # exact frame index
        GoodBye.setAutoDraw(True)
    if GoodBye.status == STARTED and frameN >= instrStopTime:
        GoodBye.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

CPT_X_responseListTotal = len([elem for elem in CPT_X_responseList if elem == '1'])
CPT_X_correctList_Total = sum(CPT_X_correctList)
CPT_X_responseTimeList_Average = (sum(CPT_X_responseTimeList)/len([elem for elem in CPT_X_responseTimeList if elem != 0]))
csvDictionary = {'CPT_X_letters': list1[1:10], 'correctButton':buttonList1[1:10], 'Response':CPT_X_responseList, 'Correct':CPT_X_correctList, 'Accuracy':CPT_X_accuracy, 'Response_Time':CPT_X_responseTimeList}
final_line = {'CPT_X_letters': 'Total:', 'correctButton':'-'*5, 'Response':CPT_X_responseListTotal, 'Correct':CPT_X_correctList_Total, 'Accuracy':'Average:', 'Response_Time':CPT_X_responseTimeList_Average}
write_data_file(csvDictionary, '%s_CPT_X_results' % expInfo['participant'], ['CPT_X_letters', 'correctButton', 'Response', 'Correct', 'Accuracy', 'Response_Time'], final_line)
CPT_AX_responseListTotal = len([elem for elem in CPT_AX_responseList if elem == '1'])
CPT_AX_correctList_Total = sum(CPT_AX_correctList)
CPT_AX_responseToAList_Total = sum(CPT_AX_responseToAList)
CPT_AX_responseTimeList_Average = (sum(CPT_AX_responseTimeList)/len([elem for elem in CPT_AX_responseTimeList if elem > 0]))
csvDictionary = {'CPT_AX_letters': list2[1:10], 'correctButton':buttonList2[1:10], 'Response':CPT_AX_responseList, 'Response_To_A':CPT_AX_responseToAList, 'Correct':CPT_AX_correctList, 'Accuracy':CPT_AX_accuracy, 'Response_Time':CPT_AX_responseTimeList}
final_line = {'CPT_AX_letters': 'Total:', 'correctButton':'-'*5, 'Response':CPT_AX_responseListTotal, 'Response_To_A': CPT_AX_responseToAList_Total,'Correct':CPT_X_correctList_Total, 'Accuracy':'Average:', 'Response_Time':CPT_X_responseTimeList_Average}
write_data_file(csvDictionary, '%s_CPT_AX_results' % expInfo['participant'], ['CPT_AX_letters', 'correctButton', 'Response', 'Response_To_A', 'Correct', 'Accuracy', 'Response_Time'], final_line)

Nback_responseListTotal = len([elem for elem in Nback_responseList if elem == '1'])
Nback_correctList_Total = sum(Nback_correctList)
Nback_responseTimeList_Average = (sum(Nback_responseTimeList)/len(elem for elem in Nback_responseTimeList if elem != 0))
csvDictionary = {'Nback_letters': oldLets, 'correctButton':correctButtonList, 'Response':Nback_responseList, 'Correct':Nback_correctList, 'Accuracy':Nback_accuracy, 'Response_Time':Nback_responseTimeList}
final_line = {'CPT_AX_letters': 'Total:', 'correctButton':'-'*5, 'Response':Nback_responseListTotal, 'Correct':Nback_correctList_Total, 'Accuracy':'Average:', 'Response_Time':Nback_responseTimeList_Average}
write_data_file(csvDictionary, '%s_Nback_results' % expInfo['participant'], ['Nback_letters', 'correctButton', 'Response', 'Correct', 'Accuracy', 'Response_Time'], final_line)
win.close()
core.quit()
