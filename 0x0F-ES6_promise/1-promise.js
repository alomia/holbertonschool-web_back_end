// Don't make a promise...if you know you can't keep it

const getFullResponseFromAPI = (success) => {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({
        status: 200,
        body: "Success",
      });
    }
    reject(new Error("The fake API is not working currently"));
  });
};

export default getFullResponseFromAPI;
