export const state = () => ({
    recycleCategories: [{
        id: 1,
        name: "Cartón",
        slug: "carton",
        img: "https://images.unsplash.com/photo-1509956563346-93a1179cea68?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"
    },
    {
        id: 2,
        name: "Plástico",
        slug: "plastico",
        img: "https://images.unsplash.com/photo-1530587191325-3db32d826c18?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=667&q=80"
    }],
    problems: [
        {
          id: 1,
            imageUrl: 'https://images.unsplash.com/photo-1565282604648-a13c5f19fd61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80',
          title: 'Cambio climático',
          description: 'Es la variación del clima de nuestro planeta, el cual siempre tuvo un comportamiento cíclico relativamente lento y en los últimos tiempos se vio abruptamente acelerado a causa del calentamiento global.',
          causes: [
            'Efecto invernadero',
            'Deforestación',
            'Destrucción de ecosistemas marinos',
            'Aumento de la población'
          ],
          consequences: [
            'Cambios en ecosistemas y desertificación',
            'Derretimiento de los polos y subida del nivel del mar',
            'Riesgos en la salud humana',
            'Especies en peligro de extinción y migraciones masivas',
            'Fenómenos meteorológicos extremos'
          ],
          howToHelp: [
            'Reducí el consumo eléctrico: apagá las luces, desenchufá los aparatos que no estés usando, usá lámparas LED, colgá la ropa en vez de usar secarropas, etc.',
            'Ahorrá agua: duchate en 5 minutos, usá el programa de lavado que use menos agua, etc.',
            'Usá los sistemas de calefacción solo si es necesario'
          ]
        },
        {
          id: 2,
            imageUrl: 'https://files.rcnradio.com/public/styles/image_834x569/public/2018-11/contaminacion_1_0.jpg?itok=UcEdvtou',
          title: 'Contaminacion',
          description: 'Es la introducción de objetos, sustancias u otros elementos al medio ambiente.',
          causes: [
            'Exceso de vehículos',
            'Exceso de productos plásticos',
            'Plaguicidas en los alimentos',
            'Exceso de residuos',
            'Falta de regulaciones'
          ],
          consequences: [
            'Riesgos en la salud humana',
            'Especies en peligro de extinción'
          ],
          howToHelp: [
            'Dejá de usar el auto y usá en lo posible transportes ecológicos como la bicicleta, o de no ser posible usá el transporte público',
            'Dejá de usar plásticos para todo: usá bandejas reusables, sorbetes de metal, botellas reusables, etc. Elegí no comprar productos que tengan plásticos innecesarios',
            'Elegí alimentos orgánicos'
          ]
        },
        {
          id: 3,
          imageUrl: 'https://www.nuevatribuna.es/media/nuevatribuna/images/2019/09/01/2019090108291259120.jpg',
          title: 'Deforestación',
          description: 'Es la tala o quema de los bosques de manera accidental o intencionada',
          causes: [
            'Fenómenos naturales',
            'Indisponibilidad de tierras',
            'Industria maderera',
            'Incendios forestales'
          ],
          consequences: [
            'Especies en peligro de extinción',
            'Desertificación de los suelos',
            'Inundaciones',
            'Calentamiento global',
            'Peor calidad de aire'
          ],
          howToHelp: [
            'Plantá árboles o contribuí con organizaciones que planten árboles',
            'Elegí productos fabricados por empresas que replantan los árboles de la madera que usan',
            'Reducí emisiones de gases nosivos para el medioambiente'
          ]
        },
        {
          id: 4,
            imageUrl: 'https://www.nuevatribuna.es/media/nuevatribuna/images/2019/09/01/2019090108291259120.jpg',
          title: 'Sobreexplotación de los recursos naturales',
          description: 'Los recursos naturales que nos provee el planeta se están derrochando irresponsablemente, y pronto ya no serán suficientes',
          causes: [
            'Aumento de la población humana',
            'Aumento de las actividades humanas y de la demanda',
            'Uso inadecuado de los recursos naturales'
          ],
          consequences: [
            'Destrucción de hábitats naturales y ecosistemas',
            'Extinción de especies',
            'Desertificación de suelos',
            'Contaminación ambiental',
            'Calentamiento global y del cambio climático'
          ],
          howToHelp: [
            'Reducí el consumo de productos que no necesitás',
            'Consumí productos locales y de temporada, en vez de productos que tengan que venir de otras partes del mundo'
          ]
        },
            {
                id: 5,
              imageUrl: 'https://www.idencityconsulting.com/wp-content/uploads/2017/10/foto-portada-800x460.png',
              title: 'Escasez de agua',
              description: 'Es la falta de suficientes recursos hídricos para satisfacer las demandas de consumo de agua en una región, y afecta a alrededor de 2800 millones de personas',
              causes: [
                'Cambio climático',
                'Uso descontrolado del agua'
              ],
              consequences: [
                'Hambre',
                'Enfermedades',
                'Especies en extinción',
                'Conflictos'
              ],
              howToHelp: [
                'Cerrá las canillas si no las estás usando',
                'Duchate en 5 minutos',
                'Cociná tratando de ahorrar agua',
                'Lavá la ropa en el modo que menos agua use'
              ]
            },
            {
                id: 6,
              imageUrl: 'https://t1.ev.ltmcdn.com/es/posts/7/3/5/que_son_los_residuos_solidos_y_como_se_clasifican_1537_600.jpg',
              title: 'Residuos',
              description: 'Es la acumulación en exceso de residuos que afectan al medio ambiente',
              causes: [
                'Aumento de la población humana',
                'Aumento de las actividades humanas',
                'Consumismo',
                'Incapacidad o ineficiencia para reciclar los residuos'
              ],
              consequences: [
                'Destrucción de hábitats naturales y ecosistemas',
                'Extinción de especies',
                'Contaminación ambiental',
                'Riesgo para la salud humana'
              ],
              howToHelp: [
                'Reducí el consumo de productos que no necesitás',
                'Reciclá'
              ]
            }
          ]
  })
