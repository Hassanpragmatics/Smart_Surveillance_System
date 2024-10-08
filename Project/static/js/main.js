let monitoring

/**
 * Function to request the server to start the motor
 */
async function requestStartMotor () {
  try {
    // Make request to server
    await axios.post('/start_motor')

    // Update status
    updateStatus('Working')
    startMonitoring()
  } catch (e) {
    console.log('Error starting the motor', e)
    updateStatus('Error starting')
  }
}

/** 
 * (Re)start monitoring
 */
async function startMonitoring () {
  monitoring = true
  while (monitoring) {
    let result = await axios.get('/monitor')
    updateMonitoringData(result.data)
    monitoring = false
  }
}

/** 
 * Stop monitoring
 */
function stopMonitoring () {
  monitoring = false
}

/**
 * Function to request monitoring data to the server and display it in the main page
 */
function updateMonitoringData (data) {
  // Get HTML elements where results are displayed
  let inZone = document.getElementById("inzone")
  let distance = document.getElementById("distance")
  inZone.innerText = data.inZone
  distance.innerText = data.distance
  // ...
}

/**
 * Function to request the server to stop the motor
 */
function stopSystem () {
  //...
  axios({
      method: 'POST',
      url: '/stop_system',
    });
  updateStatus('The motor and sensor monitoring will stop')
}


function updateStatus(statusText) {
  // Get the HTML element where the status is displayed
  let motor_status_text = document.getElementById('status_text')
  motor_status_text.innerText = statusText
}
