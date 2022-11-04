let $areas = document.getElementById('selectorArea')
let $proceso = document.getElementById('selectorProceso')
let $subproceso = document.getElementById('selectorSubproceso')
let $equiposSubproceso = document.getElementById('selectorEquipoSubproceso')

let areas = ['Criogénica', 'Estabilización', 'Turbocompresión de gas seco', 'Turbocompresión de gas húmedo', 'Compresores OVH', 'Servicios A', 'Servicios B', 'Tratamiento de agua', 'Generación eléctrica', 'Minitoping']
let procesos = ["Criogénica 1", "Criogénica 2", "Criogénica 3", "Criogénica 4", "Criogénica 5", 'Estabilización 1', 'Estabilización 2', 'Estabilización 3']
let subprocesosCrio1 = ['Acondicionamiento primario 1', 'Deshidratación 1','Separación criogénica 1']
let subprocesosCrio2 = ['Acondicionamiento primario 2', 'Deshidratación 2','Separación criogénica 2']
let subprocesosCrio3 = ['Acondicionamiento primario 3', 'Deshidratación 3','Separación criogénica 3']
let subprocesosCrio4 = ['Acondicionamiento primario 4', 'Deshidratación 4','Separación criogénica 4']
let subprocesosCrio5 = ['Acondicionamiento primario 5', 'Deshidratación 5','Separación criogénica 5']

let equiposDeshidratación1 = [
    'PAY_3220',
    'PAY_3230',
    'EAL_3120A',
    'EAL_3120B',
    'KAE_3770',
    'KAE_3775',
    'EAE_3780A',
    'EAE_3780B'
]
let equiposSeparacionCriogenica1 = [
    'PAY_4210',
    'PAY_4220',
    'KAE_4140',
    'PAY_4920',
    'PAY_4925',
    'PAY_4930',
    'EAL_4910',
    'EAL_4910B',
    'EAL_4250',
    'EAL_4260'
]
let equiposDeshidratación2 = [
    'PAY_3420',
    'PAY_3430',
    'EAL_3320A',
    'EAL_3320B',
    'KAE_3970',
    'KAE_3975',
    'EAE_3980A',
    'EAE_3980B'
]
let equiposSeparacionCriogenica2 = [
    'PAY_4410',
    'PAY_4420',
    'KAE_4340',
    'PAY_5020',
    'PAY_5025',
    'PAY_5030',
    'EAL_5010',
    'EAL_5010B',
    'EAL_4450',
    'EAL_4460'
]
let equiposDeshidratación3 = [
    'PAY_13220',
    'PAY_13230',
    'EAL_13120A',
    'EAL_13120B',
    'KAE_13770',
    'KAE_13775',
    'EAE_13780A',
    'EAE_13780B'
]
let equiposSeparacionCriogenica3 = [
    'PAY_14210',
    'PAY_14225',
    'KAE_14140',
    'PAY_14920',
    'PAY_14925',
    'PAY_14930',
    'EAL_14910',
    'EAL_14910B',
    'EAL_14250',
    'EAL_14260'
]
let equiposDeshidratación4 = [
    'PAY_13420',
    'PAY_13430',
    'EAL_13320A',
    'EAL_13320B',
    'KAE_13970',
    'KAE_13975',
    'EAE_13980A',
    'EAE_13980B'
]
let equiposSeparacionCriogenica4 = [
    'PAY_14410',
    'PAY_14425',
    'KAE_14340',
    'PAY_15020',
    'PAY_15025',
    'PAY_15030',
    'EAL_15010',
    'EAL_15010B',
    'EAL_14450',
    'EAL_14460'
]
let equiposDeshidratación5 = [
    'PAY_23220',
    'PAY_23230',
    'EAL_23120A',
    'EAL_23120B',
    'KAE_23770',
    'KAE_23775',
    'EAE_23780A',
    'EAE_23780B'
]
let equiposSeparacionCriogenica5 = [
    'PAY_24210',
    'PAY_24225',
    'KAE_24140',
    'PAY_24920',
    'PAY_24925',
    'PAY_24930',
    'PBB_24930',
    'EAL_24910',
    'EAL_24910B',
    'EAL_24250',
    'EAL_24260'
]

function mostrarLugares(arreglo, lugar){
    let elementos = '<option selected disables>-</option>'
    for(let i = 0; i < arreglo.length; i++) {
        elementos += '<option value="' + arreglo[i] +'">' + arreglo[i] +'</option>'
    }
    lugar.innerHTML = elementos
}

mostrarLugares(areas,$areas)

$areas.addEventListener('change', function(){
    let valor = $areas.value

    switch(valor){
        case 'Criogénica':
            let recortar0 = procesos.slice(0,5)
            mostrarLugares(recortar0,$proceso)
            break
        case 'Estabilización':
            let recortar1 = procesos.slice(5,8)
            mostrarLugares(recortar1, $proceso)
            break
    }
})
$proceso.addEventListener('change', function(){
    let valor =  $proceso.value
    switch(valor){
        case 'Criogénica 1':
            mostrarLugares(subprocesosCrio1,$subproceso)
            break
        case 'Criogénica 2':
            mostrarLugares(subprocesosCrio2,$subproceso)
            break
        case 'Criogénica 3':
            mostrarLugares(subprocesosCrio3,$subproceso)
            break
        case 'Criogénica 4':
            mostrarLugares(subprocesosCrio4,$subproceso)
            break
        case 'Criogénica 5':
            mostrarLugares(subprocesosCrio5,$subproceso)
            break           
    }
})
$subproceso.addEventListener('change', function(){
    let valor = $subproceso.value
    switch(valor){
        case 'Deshidratación 1':
            mostrarLugares(equiposDeshidratación1,$equiposSubproceso)
            break
        case 'Separación criogénica 1':
            mostrarLugares(equiposSeparacionCriogenica1,$equiposSubproceso)
            break
        case 'Deshidratación 2':
            mostrarLugares(equiposDeshidratación2,$equiposSubproceso)
            break
        case 'Separación criogénica 2':
            mostrarLugares(equiposSeparacionCriogenica2,$equiposSubproceso)
            break
        case 'Deshidratación 3':
            mostrarLugares(equiposDeshidratación3,$equiposSubproceso)
            break
        case 'Separación criogénica 3':
            mostrarLugares(equiposSeparacionCriogenica3,$equiposSubproceso)
            break
        case 'Deshidratación 4':
            mostrarLugares(equiposDeshidratación4,$equiposSubproceso)
            break
        case 'Separación criogénica 4':
            mostrarLugares(equiposSeparacionCriogenica4,$equiposSubproceso)
            break
        case 'Deshidratación 5':
            mostrarLugares(equiposDeshidratación5,$equiposSubproceso)
            break
        case 'Separación criogénica 5':
            mostrarLugares(equiposSeparacionCriogenica5,$equiposSubproceso)
            break
    }
})

// --------------------------------------------------------
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth() + 1; //January is 0!
var yyyy = today.getFullYear();

if (dd < 10) {
   dd = '0' + dd;
}

if (mm < 10) {
   mm = '0' + mm;
} 
    
today = yyyy + '-' + mm + '-' + dd;
document.getElementById("fechaReporte").setAttribute("max", today);
document.getElementById("fechaReporte2").setAttribute("max", today);