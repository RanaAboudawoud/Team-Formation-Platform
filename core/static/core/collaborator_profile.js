const addSkillButton = document.getElementById("add-skill");
const skillForms = document.getElementById("skill-forms");
const totalForms = document.getElementById("id_form-TOTAL_FORMS");
const removeSkillButton = document.getElementById("remove-skill");

addSkillButton.addEventListener("click", function() {
    const currentForms = skillForms.querySelectorAll(".skill-form");
    const newForm = currentForms[0].cloneNode(true);

    const formNumber = currentForms.length;

    newForm.innerHTML = newForm.innerHTML.replaceAll("-0-", `-${formNumber}-`);

    newForm.innerHTML = newForm.innerHTML.replaceAll("_0_", `_${formNumber}_`);

    skillForms.insertBefore(newForm, addSkillButton);

    totalForms.value = formNumber + 1;
});

removeSkillButton.addEventListener("click", function() {
    const currentForms = skillForms.querySelectorAll(".skill-form");

    if (currentForms.length > 1) {
        currentForms[currentForms.length - 1].remove();
        totalForms.value = currentForms.length - 1;
    }
})