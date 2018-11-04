<template>
  <div id="app">
    <div class="container">
      <div class="row mt-3">
        <div class="col">
          <h2 class="text-center" style="color:#0074D9">
            МАЪЛУМОТЛАР ИНТЕЛЛЕКТУАЛ ТАҲЛИЛИДАН ФОЙДАЛАНИБ МАТНЛАРНИ ТАСНИФЛАШ
          </h2>
          <div class="form-group">
            <label for="content" class="text-info">Қуйидаги майдонга матн киритинг ва таснифлаш тугмасини босинг</label>
            <textarea v-model="content" class="form-control" id="content" rows="10" placeholder="Матн киритинг"></textarea>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <button @click="send" class="btn text-white" style="background:#0074D9">Таснифлаш</button>
        </div>
      </div>
      <hr>
      <div class="row">
        <div class="col-6">          
          <canvas id="barChart"></canvas>
        </div>
        <div class="col-6">
          <table class="table table-sm">            
            <tbody>
              <tr v-for="d in dict" v-bind:key="d[0]">
                <td>{{ d[0] }}</td>
                <td>{{ (d[1]*100).toFixed() }}%</td>
              </tr>    
            </tbody>
        </table>          
        </div>
      </div>      
    </div>    
  </div>  
</template>

<script>
import Axios from 'axios'
import Chart from 'chart.js'

export default {  
  name: 'app',
  data(){
    return {
      content: '',
      labels: [],
      data: [],
      dict: []
    }    
  },
  
  methods: {
    send(){
      Axios.post('http://127.0.0.1:5000/', {content: this.content})
      .then(resp =>{
            this.labels = resp.data.labels;
            this.data = resp.data.data;
            this.dict = resp.data.dict;
            this.create_chart();
          }          
        );      
    },       
    create_chart(){
      var bc = document.getElementById("barChart").getContext('2d');
         
      var barChart = new Chart(bc, {
          type: 'bar',
          data: {
              labels: this.labels,
              datasets: [{
                  label: 'Синф эҳтимоллиги',
                  data: this.data,
                  backgroundColor: [
                      'rgba(255,220,0, 0.6)',
                      'rgba(57,204,204, 0.6)',
                      'rgba(1,255,112, 0.6)',
                      'rgba(255,65,54, 0.6)',
                      'rgba(240,18,190, 0.6)',
                      'rgba(17,17,17, 0.6)'                       
                  ],
                  borderColor: [
                      'rgba(255,220,0, 1)',
                      'rgba(57,204,204, 1)',
                      'rgba(1,255,112, 1)',
                      'rgba(255,65,54, 1)',
                      'rgba(240,18,190, 1)',
                      'rgba(17,17,17, 1)'                      
                  ],
                  borderWidth: 1
              }]
          },
          options: {
              scales: {
                  yAxes: [{
                      ticks: {
                          beginAtZero:true
                      }
                  }]
              },
              events: []
          }
      });
      
    }    

    
  } 
}
</script>

<style>
  tr:first-child {
    background: #01FF70;
  }
</style>
