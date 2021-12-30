function load_handler()
{
    if (document.readyState == 'complete')
    {
        console.log('loaded');
    }
};

window.addEventListener("load", load_handler);
