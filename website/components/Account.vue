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
    <!--    <b-card-->
    <!--      class="mx-2"-->
    <!--      border-variant="danger"-->
    <!--      header-border-variant="danger"-->
    <!--      header-text-variant="danger"-->
    <!--    >-->
    <!--      <template #header>-->
    <!--        <div class="row">-->
    <!--          <p class="mb-0">{{ accName }}</p>-->
    <!--          <div class="flex-fill"></div>-->
    <!--          <p class="mb-0">{{ accType }}</p>-->
    <!--        </div>-->
    <!--      </template>-->
    <!--      <b-card-body>-->
    <!--        <b-card-title>(${{amount}})</b-card-title>-->
    <!--        <b-button-group size="lg">-->
    <!--          <b-button variant="info">Edit</b-button>-->
    <!--          <b-button variant="danger">Delete</b-button>-->
    <!--        </b-button-group>-->
    <!--      </b-card-body>-->
    <!--    </b-card>-->
<!--    <b-list-group>-->
<!--      <b-list-group-item>Cras justo odio</b-list-group-item>-->
<!--      <b-list-group-item>Dapibus ac facilisis in</b-list-group-item>-->
<!--      <b-list-group-item>Morbi leo risus</b-list-group-item>-->
<!--      <b-list-group-item>Porta ac consectetur ac</b-list-group-item>-->
<!--      <b-list-group-item>Vestibulum at eros</b-list-group-item>-->
<!--    </b-list-group>-->
<!--    <b-card-->
<!--      class="mx-2"-->
<!--      border-variant="success"-->
<!--      header-border-variant="success"-->
<!--      header-text-variant="success"-->
<!--    >-->
<!--      <template #header>-->
<!--        <div class="row">-->
<!--          <p class="mb-0">{{ accName }}</p>-->
<!--          <div class="flex-fill"></div>-->
<!--          <p class="mb-0">{{ accType }}</p>-->
<!--        </div>-->
<!--      </template>-->
<!--      <b-card-body>-->
<!--        <b-card-title>${{ amount }}</b-card-title>-->
<!--        <b-button-group size="lg">-->
<!--          <b-button variant="info">Edit</b-button>-->
<!--          <b-button variant="danger">Delete</b-button>-->
<!--        </b-button-group>-->
<!--      </b-card-body>-->
<!--    </b-card>-->
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
