onload = function() {
  if ('speechSynthesis' in window) with(speechSynthesis) {

    var playEle = document.querySelector('#play');
    var pauseEle = document.querySelector('#pause');
    var stopEle = document.querySelector('#stop');
    var flag = false;

    playEle.addEventListener('click', onClickPlay);
    pauseEle.addEventListener('click', onClickPause);
    stopEle.addEventListener('click', onClickStop);

    var synth, utterance;
    var halted = false;

    function onClickPlay() {
      if (!flag) {
        flag = true;
        synth = window.speechSynthesis;
        utterance = new SpeechSynthesisUtterance(document.querySelector('article').innerText);
        utterance.voice = synth.getVoices()[5];
        utterance.rate = 0.7;

        playEle.className = 'played';
        stopEle.className = '';
        synth.speak(utterance);
        utterance.onend = function() {
          flag = false;
          playEle.className = pauseEle.className = '';
          stopEle.className = 'stopped';
        };
      }
      if (synth.paused || halted) { /* unpause/resume narration */
          playEle.className = 'played';
          pauseEle.className = '';
          halted = false;
          synth.resume();
          utterance.onend = function() {
            flag = false;
            playEle.className = pauseEle.className = '';
            stopEle.className = 'stopped';
          };
      }
    }

    function onClickPause() {
      if (synth.speaking && !synth.paused) { /* pause narration */
        pauseEle.className = 'paused';
        playEle.className = '';
        synth.pause();
        halted = true;
      }
    }

    function onClickStop() {
      if (synth.speaking) { /* stop narration */
        /* for safari */
        halted = false;
        stopEle.className = 'stopped';
        playEle.className = pauseEle.className = '';
        flag = false;
        synth.cancel();
      }
    }

  }

  else { /* speech synthesis not supported */
    msg = document.createElement('h5');
    msg.textContent = "Detected no support for Speech Synthesis";
    msg.style.textAlign = 'center';
    msg.style.backgroundColor = 'red';
    msg.style.color = 'white';
    msg.style.marginTop = msg.style.marginBottom = 0;
    document.body.insertBefore(msg, document.querySelector('div'));
  }

}

function readClue(id) {
    index = id-1;
    let msg = document.getElementsByClassName("clueDiv")[index].innerText;
    let speech = new SpeechSynthesisUtterance();
    speech.lang = "en.US";
    //speech.voice = getVoices()[5];
    speech.text = msg;
    speech.volume = 1;
    speech.rate = 0.8;
    speech.pitch = 1;
    let synth = window.speechSynthesis;
    speech.voice = synth.getVoices()[5];
    synth.speak(speech);
}

function readPage() {
    index = id-1;
    let msg = document.getElementsByTagName("article")[0].innerText;
    let speech = new SpeechSynthesisUtterance();
    speech.lang = "en.US";
    //speech.voice = getVoices()[5];
    speech.text = msg;
    speech.volume = 1;
    speech.rate = 0.8;
    speech.pitch = 1;
    let synth = window.speechSynthesis;
    speech.voice = synth.getVoices()[5];
    synth.speak(speech);
}
