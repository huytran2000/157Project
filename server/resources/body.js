const ipAddr = "127.0.0.1"
const portNum = "8080"

const url = "http://" + ipAddr + ":" + portNum + "/get?query="

const button = document.getElementById("bt")
const textField = document.getElementById("tx-field")
const statusIconImg = document.getElementById("status-icon")
const statusTextDiv = document.getElementById("status-text")
const recordedQueryDiv = document.getElementById("query-read")
const resDiv = document.getElementById("response")

function parseResponse(res) {
    let parsed = []
    for (let row of res.split("\n")) {
        let elems = []
        for (let e of row.split("|")) {
            elems.push(e)
        }
        parsed.push(elems)
    }
    return { headers: parsed[0], data: parsed.slice(1, parsed.length) }
}

function populateTableHeaders(table, headers) {
    let thead = table.createTHead()
    let row = thead.insertRow()
    for (let head of headers) {
        let th = document.createElement("th")
        let text = document.createTextNode(head)
        th.appendChild(text)
        row.appendChild(th)
    }
}

function populateTableEntries(table, data) {
    for (let dataRow of data) {
        let row = table.insertRow() // automatically generate TBody if TBody DN exist (check doc)
        for (let dataCell of dataRow) {
            let td = document.createElement("td")
            let text = document.createTextNode(dataCell)
            td.appendChild(text)
            row.appendChild(td)
        }
    }
}

button.addEventListener("click", async () => {
    let query = textField.value
    query = query.trim()
    // waiting behavior
    recordedQueryDiv.innerHTML = "Your query: " + query
    statusIconImg.src = "/server/images/loading.gif"
    button.classList.add("event-disabled")
    resDiv.textContent = ""

    // check for select statement
    if (!query.toLowerCase().startsWith("select")) {
        statusIconImg.src = "/server/images/red-cross.jpg"
        statusTextDiv.innerHTML = "Query failed: Only 'select' statement will be accepted"
        statusTextDiv.style.color = 'red'
        button.classList.remove("event-disabled")
        textField.select()
        //textField.style.borderColor = "red";
        return
    }
    // send request to server
    let responsePromise
    try {
        responsePromise = await fetch(url + query)
    } catch (error) {
        statusIconImg.src = "/server/images/red-cross.jpg"
        statusTextDiv.innerHTML = "Query failed: Can not reach server"
        statusTextDiv.style.color = 'red'
        button.classList.remove("event-disabled")
        return
    }
    let response = await responsePromise.text().then((text) => { return text })

    // only check if DB recognizes query from "Response from server: " custom error msg, for simplicity
    switch (response.startsWith("Response from server: ")) {
        case true: // DB does not recognize query
            statusIconImg.src = "/server/images/red-cross.jpg"
            statusTextDiv.innerHTML = "Query failed: " + response
            statusTextDiv.style.color = 'red'
            textField.select()
            break
        default: // Query successful
            statusIconImg.src = "/server/images/green-mark.jpg"
            statusTextDiv.innerHTML = "Query successful!"
            statusTextDiv.style.color = 'green'
            // create table DOM element
            let parsedResponse = parseResponse(response)
            let tbl = document.createElement('table')
            populateTableHeaders(tbl, parsedResponse.headers)
            populateTableEntries(tbl, parsedResponse.data)
            resDiv.appendChild(tbl)
    }
    button.classList.remove("event-disabled")

})
