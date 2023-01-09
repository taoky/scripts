// https://github.com/ubuntu/gnome-shell-extension-appindicator/issues/294#issuecomment-971161515
// Copy to clipboard first
// Alt + F2, 'lg'

let boxes = [
    ...imports.ui.main.panel._rightBox.get_children(),
    ...imports.ui.main.panel._leftBox.get_children(),
    ...imports.ui.main.panel._centerBox.get_children()
];
for (var v of boxes) {
    let fc = v.first_child?.first_child?.first_child;
    if (fc && fc.window === null) { v.destroy(); }
};
