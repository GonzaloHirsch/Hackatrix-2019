<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col md="6" lg="8">
        <div class="pl-6 display-1">
          Tips
        </div>
      </v-col>
    </v-row>

    <v-row justify="center" dense class="pb-8 pl-6 pr-6 mb-n8">
      <v-col md="6" lg="8">
        <v-select
          chips
          label="Tipo de Tip"
          multiple
          solo
          :items="filterChips"
          clearable
          deletable-chips
          @change="chipFilterAdded"
          menu-props="offsetY"
        >
        </v-select>
      </v-col>
    </v-row>

    <div v-for="item in items" class="pb-8" :hidden="item.hidden">
      <v-row justify="center">
        <v-col md="6" lg="8">
          <div class="pl-6 headline">{{ item.type }}</div>
        </v-col>
      </v-row>

      <v-row justify="center">
        <v-col md="6" lg="8">
          <v-expansion-panels popout>
            <Tip
              v-for="tip in item.tips"
              :key="tip.title"
              :title="tip.title"
              :items="tip.items"
              :counter="tip.counter"
            ></Tip>
          </v-expansion-panels>
         </v-col>
       </v-row>
    </div>
  </v-container>
</template>

<script>
  import Tip from "../components/Tip";

  export default {
    name: "tip.vue",
    components: { Tip },
    data() {
      return {
        items: [],
        filterChips: []
      };
    },
    async mounted() {
      await this.loadTips();
      this.filterChips = [];
      for (let item of this.items) {
        this.filterChips.push({
          text: item.type,
          value: item.type
        })
      }
    },
    methods: {
      async loadTips() {
        try {
          let items = (await this.$axios.$get("/tips"));
          if (items != null) this.items = items;
        } catch (e) {
          console.error(e);
          this.items = [
            {
              "type": "En el día a día",
              "tips": [
                {
                  "title": "Ahorrá energía",
                  "counter": 1,
                  "items": [
                    "Desenchufá los equipos y aparatos que no están en uso",
                    "Apagá las luces que no necesites",
                    "Usá la calefacción solamente si es necesario",
                    "Colgá la ropa en vez de usar secarropas",
                    "Tapá las ollas al hervir agua para usar menos gas/electricidad"
                  ]
                },

                {
                  "title": "Ahorrá agua",
                  "counter": 1,
                  "items": [
                    "Cerrá las canillas si no las estás usando",
                    "Duchate en 5 minutos",
                    "Cociná tratando de ahorrar agua",
                    "Lavá la ropa en el modo que menos agua use"
                  ]
                },

                {
                  "title": "Contaminá menos",
                  "counter": 3,
                  "items": [
                    "Reemplazá el auto por transportes más ecológicos como la bicicleta, o de no ser posiblé usá el transporte público",
                    "Evitá los plásticos innecesarios: usá bandejas reusables, no compres productos con mucho plástico",
                    "Elegí alimentos orgánicos"
                  ]
                },

                {
                  "title": "Ayuda a ayudar",
                  "counter": 1,
                  "items": [
                    "Corré la voz: alentá a tus conocidos a ayudar también!"
                  ]
                }



              ]
            },

            {
              "type": "Para hacer una vez",
              "tips": [
                {
                  "title": "Ahorrá energía",
                  "counter": 3,
                  "items": [
                    "Cambiá tus lámparas por LED",
                    "Instalá paneles solares",
                    "Instalá un termotanque solar",
                    "Elegí electrodomésticos más eficientes"
                  ]
                },

                {
                  "title": "Contaminá menos",
                  "counter": 5,
                  "items": [
                    "Reciclá los envases plásticos y empezá a usar envases de vidrio o metal"
                  ]
                }
              ]
            },

            {
              "type": "Para hacer de vez en cuando",
              "tips": [
                {
                  "title": "Desde casa",
                  "counter": 5,
                  "items": [
                    "Buscá cosas que no uses y que se puedan reciclar"
                  ]
                },

                {
                  "title": "Desde donde estés",
                  "counter": 5,
                  "items": [
                    "Doná a alguna organización que ayude al medio ambiente"
                  ]
                }
              ]
            }
          ];
        }
      },
      chipFilterAdded(chips) {
        if (chips.length === 0) {
          for (let item of this.items) {
            if (item.hidden) item.hidden = false;
          }
        } else {
          for (let item of this.items) {
            let index = chips.indexOf(item.type);
            if (index !== -1) {
              if (item.hidden) item.hidden = false;
            } else {
              if (!item.hidden) item.hidden = true;
            }
          }
        }
      }
    }
  }
</script>

<style scoped>

</style>
