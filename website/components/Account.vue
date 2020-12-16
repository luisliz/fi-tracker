<template>
    <b-list-group-item>
      <b-row>
        <b-col>
          <div class="font-weight-bold">
            {{accName}}
          </div>
          <div class="text-muted small">
            {{accType}}
          </div>
        </b-col>
        <b-col align-self="center" v-if="accIsLiability">
         (${{amount}})
        </b-col>
        <b-col align-self="center" v-else>
          ${{amount}}
        </b-col>
      </b-row>
    </b-list-group-item>
</template>
<script lang="ts">
export default {
  props: {
    accName: {
      type: String,
      default: 'ACC',
      required: true
    },
    accType: {
      type: String,
      default: 'TYPE',
      required: true
    },
    accIsLiability: {
      type: Boolean,
      default: false
    },
    amount: {
      type: Number,
      required: true
    }
  },
  data() {
    const message: string = 'This is a message'

    return {
      message
    }
  }
}
</script>
<style>
.nuxtlogo {
  animation: 1s appear;
  margin: auto;
}

@keyframes appear {
  0% {
    opacity: 0;
  }
}
</style>
