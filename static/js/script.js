function launchBlackBox() {
  document.querySelector('.start-btn').style.display = 'none';
  document.querySelector('.terminal').classList.remove('hidden');
  document.getElementById('bg-audio').play();

  const terminal = new Typed("#typed", {
    strings: [
      "Initializing backdoor...",
      "Evading trace... spoofing MAC...",
      "Connected to darknet relay [89.203.45.22]",
      "Accessing classified logs...",
      "🔥 root@federalnode-01 breached",
      "Leaking facial ID cache...",
      "Injecting payload: rm -rf / --no-preserve-root",
      ">>> Data corruption: 73% complete",
      "Activating cloaking protocol",
      "BlackBox is now invisible. You were never here 💀"
    ],
    typeSpeed: 40,
    backSpeed: 0,
    loop: false,
    showCursor: false
  });
}
