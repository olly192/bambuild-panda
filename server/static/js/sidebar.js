const sidebar = document.getElementById("sidebar")
const sidebarToggle = document.getElementById("sidebar-toggle")

if (sidebar && sidebarToggle) {
    console.log("sidebar and sidebarToggle exist")
    sidebarToggle.addEventListener("click", () => {
        if (sidebar.style.minWidth){
            sidebar.style.minWidth = null;
        } else {
            sidebar.style.minWidth = "16rem";
        }
        sidebarToggle.children[0].classList.toggle("fa-bars")
        sidebarToggle.children[0].classList.toggle("fa-xmark")
    })

    let sidebarCollapse = document.getElementsByClassName("sidebar-collapse");

    for (let i = 0; i < sidebarCollapse.length; i++) {
        sidebarCollapse[i].addEventListener("click", function() {
            this.classList.toggle("active");
            let content = this.nextElementSibling;
            if (content.style.maxHeight){
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    }
}