const sidebar = document.getElementById("sidebar")
const sidebarToggle = document.getElementById("sidebar-toggle")
let sidebarCollapse = document.getElementsByClassName("sidebar-collapse")
let sidebarOpen = true
function setSidebar(open) {
    if (open){
        sidebar.style.minWidth = "16rem"
        sidebarToggle.children[0].classList.remove("fa-bars")
        sidebarToggle.children[0].classList.add("fa-xmark")
    } else {
        sidebar.style.minWidth = null
        for (let i = 0; i < sidebarCollapse.length; i++) {
            sidebarCollapse[i].classList.remove("active")
            sidebarCollapse[i].nextElementSibling.style.minHeight = null
        }
        sidebarToggle.children[0].classList.add("fa-bars")
        sidebarToggle.children[0].classList.remove("fa-xmark")
    }
    sidebarOpen = open
}

if (sidebar && sidebarToggle) {
    sidebar.style.transition = "none"
    if (window.innerWidth < 1024) {
        setSidebar(false)
    } else {
        setSidebar(true)
    }
    sidebar.style.transition = null
    sidebarToggle.addEventListener("click", () => setSidebar(!sidebarOpen))
}