let nameInput = document.querySelector('[name=name]')
let first_name = getParams()['first_name']
nameInput.value = first_name

const handleNameInput = () => {
    if (nameInput.value.length == 0) {
        webapp.MainButton.hide()
        return
    }
    webapp.MainButton.show();
    webapp.MainButton.text = "Create " + nameInput.value + "'s Name Card";
}

nameInput.addEventListener('input', handleNameInput)


handleNameInput()


webapp.MainButton.onClick( () => {
    webapp.sendData(JSON.stringify({
        action: "create_name_card",
        name: nameInput.value,
        usepic: document.querySelector('[name=usepic]').checked,
    }))
})