/**
 * Theme: Unikit - Responsive Bootstrap 5 Admin Dashboard
 * Author: Mannatthemes
 * Dropzone Js
 */
const handleChange = function() {
  const fileUploader = document.querySelector('#input-file');
      const getFile = fileUploader.files
      if (getFile.length !== 0) {
          const uploadedFile = getFile[0];
          readFile(uploadedFile);
          form = new FormData();
          form.append('file', uploadedFile);
          fetch('http://localhost:8000/prediction', {
              method: 'POST',
              body: form
          }).then(response => {
            response.json()
            .then(data => {
              const parent = document.querySelector('.pr-box');
              parent.innerHTML = parent.innerHTML + `<h4 class = "col-6" style = "margin-left:10px;">${data.text}</h4>`;
              
          });
        
      });
  }
}
  const readFile = function (uploadedFile) {
      if (uploadedFile) {
          const reader = new FileReader();
          reader.onload = function () {
          const parent = document.querySelector('.pr-box');
          parent.innerHTML = `<img  style = "height: 212px;
          max-width: 100%;
          border-radius: 5px;float:left;"  src=${reader.result}  />`;

          };
          
          reader.readAsDataURL(uploadedFile);
      }
  };


  var uppy = Uppy.Core({
    locale: {
      strings: {
        closeModal: "Модалды теріден шығу",
        importFrom: "%{name} деректерін импорттау",
        addingMoreFiles: "Көбірек файлдарды қосу",
        addMoreFiles: "Көбірек файлдарды қосу",
        dashboardWindowTitle: "Файл жүктеу терезесі (Шығу үшін escape түймесін басыңыз)",
        dashboardTitle: "Файл жүктеу",
        copyLinkToClipboardSuccess: "Сілтеме ашық тақтаны скопиялау",
        copyLinkToClipboardFallback: "Төменгі URL мекенжайын көшіріңіз",
        copyLink: "Сілтемені көшіру",
        fileSource: "Файл көзі: %{name}",
        done: "Аяқталды",
        back: "Артқа",
        addMore: "Көбірек қосу",
        removeFile: "Файлды алып тастау",
        editFile: "Файлды өңдеу",
        editing: "%{file}ды өңдеу",
        finishEditingFile: "Файлды өңдеуді аяқтау",
        saveChanges: "Өзгерістерді сақтау",
        cancel: "Болдырмау",
        myDevice: "Менің құрылғым",
        dropPasteFiles: "Файлдарды осында атқарыңыз, қою немесе %{browseFiles}",
        dropPasteFolders: "Файлдарды осында атқарыңыз, қою немесе %{browseFolders}",
        dropPasteBoth: "Файлдарды осында атқарыңыз, қою, %{browseFiles} немесе %{browseFolders}",
        dropPasteImportFiles: "Файлдарды осында атқарыңыз, қою, %{browseFiles} немесе шулай импорттау:",
        dropPasteImportFolders: "Файлдарды осында атқарыңыз, қою, %{browseFolders} немесе шулай импорттау:",
        dropPasteImportBoth: "Файлдарды осында атқарыңыз, қою, %{browseFiles}, %{browseFolders} немесе шулай импорттау:",
        dropHint: "Файлдарыңызды осында атқарыңыз",
        browseFiles: "файлдарды таңдау",
        browseFolders: "папкаларды таңдау",
        uploadComplete: "Жүктеу аяқталды",
        uploadPaused: "Жүктеу тоқтатылды",
        resumeUpload: "Жүктеуді жалғастыру",
        pauseUpload: "Жүктеуді тоқтату",
        retryUpload: "Жүктеуді қайталау",
        cancelUpload: "Жүктеуді болдырмау",
        xFilesSelected: {
            0: "%{smart_count} файл таңдалды",
            1: "%{smart_count} файл таңдалды"
        },
        uploadingXFiles: {
            0: "%{smart_count} файл жүктелуде",
            1: "%{smart_count} файл жүктелуде"
        },
        processingXFiles: {
            0: "%{smart_count} файл өңделуде",
            1: "%{smart_count} файл өңделуде"
        },
        poweredBy2: "%{backwardsCompat} %{uppy}",
        poweredBy: "Мысалы"
    }
    
    }
  })
  
  
  .use(Uppy.Dashboard, {
    inline: true,
    target: '#drag-drop-area'
  })
  .use(Uppy.XHRUpload, { endpoint: 'http://localhost:8000/clasification', fieldName: 'file' })


uppy.on('complete', function (result) {
  const successfulFiles = result.successful;
  successfulFiles.forEach(file => {
    const preview = file.preview;
    console.log(file)
    console.log(file.response.body.class)
      const parent = document.getElementById('grid');
      parent.innerHTML = parent.innerHTML + `<div class="col-md-4 col-lg-3 picture-item" data-groups='["${file.response.body.class}"]'>
      <a href="${preview}" class="lightbox">
          <img src="${preview}" alt="" class="img-fluid" />
      </a>  
  </div>`;
  
 
var Shuffle = window.Shuffle;
  setTimeout(() => {
  window.demo = new Demo(document.getElementById('grid'));
  },100);
  console.log()

  });
})

