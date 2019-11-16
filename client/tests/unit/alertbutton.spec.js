import { shallowMount } from "@vue/test-utils";
import AlertButton from "../../src/components/AlertButton.vue";

describe("AlertButton.vue", () => {
  it("renders props.msg when passed", () => {
    const msg = "new message";
    const wrapper = shallowMount(AlertButton, {
      propsData: { msg }
    });
    expect(wrapper.text()).toMatch(msg);
  });
});
