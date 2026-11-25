import projects from './projects.json';
import images from './images.json';
import captions from './captions.json';
export { projects, images, captions };
export const groups = [['series','Series','Our big projects ...'],['collaboration-projects','Collaboration projects','Our collaboration projects mostly with Latvian fashion designers and other artists'],['specials','Specials',"The ones, that haven't found a place in other categories, but are no less important to us"]];
export const groupName = Object.fromEntries(groups.map(g=>[g[0],g[1]]));
export const img = id => images[id] || { w: 3, h: 2 };
