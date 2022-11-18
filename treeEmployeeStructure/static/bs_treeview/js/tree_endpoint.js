document.addEventListener('DOMContentLoaded', function () {
        NavTree.createBySelector("#nav-tree", {
        showEmptyGroups: true,

        groupOpenIconClass: "fas",
        groupOpenIcon: "fa-chevron-down",

        groupCloseIconClass: "fas",
        groupCloseIcon: "fa-chevron-right",

        linkIconClass: "fas",
        linkIcon: "fa-link",

        iconPlace: "start"
    });
});