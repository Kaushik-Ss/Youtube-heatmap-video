# Youtube-heatmap-video
Crops the best part of the video and open it in a new tab 
- Uses selenium
- Special thanks to [listenonrepeat](https://listenonrepeat.com) and [socalvideoplaza](https://www.socialvideoplaza.com/en/tools/embed-code-link-generator) for making this possible
- Contians unremoved comment to understand the flow of the program and why I choose x instead of y


# Future plans
- Refactor un-used libraries 
- Refactor methods to new implementation

# Problems that I faced during creation
- YouTube provides YouTube creators a option to enable embed videos and it seems youtube api removed free access to embed youtube while it is still supported by some videos that were uploaded before 2010. So I had to use alternatives to make the video start at a specific moment so I had to use a third party website
- YouTube heapmap anaylsis was recently made public early 2022 while it was avaibale from late 2021 for testing and beta creators [source](https://htxt.co.za/2021/12/youtube-is-testing-a-heatmap-and-were-in-two-minds-about-it/)
so that was one of the reason I didnt make this repo public because youtube heatmap component was not avaivale for all videos but after anaylsing some of the video I found it showed a straight line for some reason this maybe changed when the repo becomes public
- Had to manually find and test each compnent by different methods and was using a old selenium methods by practice so some methods are refactoed but still some old/depreciated methods are used in this repo.
