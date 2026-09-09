easy web

i check the source page and see the main.js file

after checking it i see that condition:
```javascript
if (availableOptions[currentStep].includes(currentCommand) || availableOptions['secret'].includes(currentCommand))
```

That means there a secret command i need to find.
Scrolling down i see where the `availableOptions` are fetched from.
This api call : 
`/api/options`

when i fetch it manually, i find the secret command :
`Blip-blop, in a pickle with a hiccup! Shmiggity-shmack`

then i paste it in the terminal and got the flag.
